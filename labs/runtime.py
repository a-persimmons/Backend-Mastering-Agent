"""Teaching baseline: bounded agent loop, explicit tool policy, fake model and durable step journal.
No network or API key required. Python 3.11+.
Not a production framework: SQLite journal is single-process; external services must
implement idempotency independently. Never run arbitrary model-generated commands.
"""
from __future__ import annotations

import asyncio
import json
import sqlite3
from dataclasses import dataclass, field
from typing import Any, Awaitable, Callable, Protocol


@dataclass(frozen=True)
class Call:
    id: str
    name: str
    args: dict[str, Any]


@dataclass(frozen=True)
class Final:
    text: str


@dataclass
class Run:
    id: str
    tenant: str
    messages: list[dict[str, Any]] = field(default_factory=list)


class Model(Protocol):
    async def next(self, run: Run) -> Call | Final: ...


class FakeModel:
    async def next(self, run: Run) -> Call | Final:
        await asyncio.sleep(0.01)
        if not any(m["role"] == "tool" for m in run.messages):
            return Call("status-1", "status", {"service": "db"})
        last = run.messages[-1]["content"]
        return Final(f"诊断结果：{last}")


class Journal:
    def __init__(self, path: str = ":memory:") -> None:
        self.db = sqlite3.connect(path)
        self.db.execute(
            "CREATE TABLE IF NOT EXISTS step (tenant TEXT, run TEXT, call TEXT, "
            "signature TEXT, result TEXT, PRIMARY KEY(tenant, run, call))"
        )

    def read(self, run: Run, call: Call) -> dict | None:
        row = self.db.execute(
            "SELECT signature, result FROM step WHERE tenant=? AND run=? AND call=?",
            (run.tenant, run.id, call.id),
        ).fetchone()
        if row is None:
            return None
        if row[0] != self.signature(call):
            raise ValueError("call_id reused with different arguments")
        return json.loads(row[1])

    @staticmethod
    def signature(call: Call) -> str:
        return json.dumps([call.name, call.args], sort_keys=True)

    def save(self, run: Run, call: Call, result: dict) -> None:
        with self.db:
            self.db.execute(
                "INSERT INTO step VALUES(?,?,?,?,?)",
                (run.tenant, run.id, call.id, self.signature(call), json.dumps(result)),
            )

    def close(self) -> None:
        self.db.close()


Tool = Callable[[dict[str, Any]], Awaitable[dict[str, Any]]]


class Dispatcher:
    def __init__(self, journal: Journal, limit: int = 4) -> None:
        if limit < 1:
            raise ValueError("limit must be positive")
        self.journal = journal
        self.slots = asyncio.Semaphore(limit)
        self.tools: dict[str, Tool] = {"status": self.status}
        self.active = 0
        self.peak = 0
        self.executions = 0

    async def status(self, args: dict) -> dict:
        await asyncio.sleep(0.02)
        return {"service": args["service"], "healthy": False}

    async def dispatch(self, run: Run, call: Call) -> dict:
        if call.name not in self.tools:
            return {"error": "denied_or_unknown_tool"}
        if set(call.args) != {"service"} or call.args["service"] not in ("db", "api"):
            return {"error": "invalid_args"}
        # Teaching simplification: reuse already committed results
        # by rechecking the journal after obtaining a slot (not a per-call lock).
        # Only read-only tools are registered; concurrent duplicates may execute twice.
        cached = self.journal.read(run, call)
        if cached is not None:
            return cached
        async with self.slots:
            cached = self.journal.read(run, call)
            if cached is not None:
                return cached
            self.active += 1
            self.peak = max(self.peak, self.active)
            self.executions += 1
            try:
                async with asyncio.timeout(1):
                    result = await self.tools[call.name](call.args)
                cached = self.journal.read(run, call)
                if cached is not None:
                    return cached
                self.journal.save(run, call, result)
                return result
            except TimeoutError:
                return {"error": "tool_timeout"}
            finally:
                self.active -= 1


class Runtime:
    def __init__(self, model: Model, dispatcher: Dispatcher, limit: int = 8) -> None:
        if limit < 1:
            raise ValueError("limit must be positive")
        self.model = model
        self.dispatcher = dispatcher
        self.slots = asyncio.Semaphore(limit)

    async def execute(self, run: Run, max_steps: int = 5, deadline: float = 3) -> dict:
        try:
            # Deadline includes waiting for a run slot.
            async with asyncio.timeout(deadline):
                async with self.slots:
                    for _ in range(max_steps):
                        decision = await self.model.next(run)
                        if isinstance(decision, Final):
                            return {"status": "succeeded", "text": decision.text}
                        run.messages.append({"role": "assistant", "call_id": decision.id,
                                             "name": decision.name, "args": decision.args})
                        result = await self.dispatcher.dispatch(run, decision)
                        run.messages.append({"role": "tool", "call_id": decision.id,
                                             "content": result})
                    return {"status": "failed", "reason": "step_budget"}
        except TimeoutError:
            return {"status": "failed", "reason": "deadline"}
        # CancelledError propagates; the service layer must persist cancelled status.


async def main() -> None:
    journal = Journal()
    try:
        dispatcher = Dispatcher(journal, limit=4)
        runtime = Runtime(FakeModel(), dispatcher)
        results = await asyncio.gather(*(runtime.execute(Run(str(i), "demo")) for i in range(20)))
        print(json.dumps({"success": sum(r["status"] == "succeeded" for r in results),
                          "peak_tool_concurrency": dispatcher.peak}, ensure_ascii=False))
    finally:
        journal.close()


if __name__ == "__main__":
    asyncio.run(main())
