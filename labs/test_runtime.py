import asyncio
import os
import tempfile
import unittest

from runtime import Call, Dispatcher, FakeModel, Journal, Run, Runtime


class EndlessModel:
    async def next(self, run):
        return Call("same", "status", {"service": "db"})


class RuntimeTests(unittest.IsolatedAsyncioTestCase):
    async def asyncSetUp(self):
        self.journal = Journal()
        self.dispatcher = Dispatcher(self.journal, limit=2)
        self.runtime = Runtime(FakeModel(), self.dispatcher, limit=5)

    async def asyncTearDown(self):
        self.journal.close()

    async def test_success_and_concurrency(self):
        results = await asyncio.gather(
            *(self.runtime.execute(Run(str(i), "tenant-a")) for i in range(12))
        )
        self.assertTrue(all(r["status"] == "succeeded" for r in results))
        self.assertLessEqual(self.dispatcher.peak, 2)

    async def test_step_budget(self):
        runtime = Runtime(EndlessModel(), self.dispatcher)
        result = await runtime.execute(Run("run", "a"), max_steps=3)
        self.assertEqual(result["reason"], "step_budget")
        self.assertEqual(self.dispatcher.executions, 1)

    async def test_policy(self):
        run = Run("run", "a")
        self.assertEqual((await self.dispatcher.dispatch(run, Call("1", "delete", {})))["error"],
                         "denied_or_unknown_tool")
        self.assertEqual((await self.dispatcher.dispatch(run, Call("2", "status", {"service": 1})))["error"],
                         "invalid_args")
        self.assertEqual(self.dispatcher.executions, 0)

    async def test_deadline_and_cancellation(self):
        result = await self.runtime.execute(Run("deadline", "a"), deadline=0.001)
        self.assertEqual(result["reason"], "deadline")
        task = asyncio.create_task(self.runtime.execute(Run("cancel", "a")))
        await asyncio.sleep(0.015)
        task.cancel()
        with self.assertRaises(asyncio.CancelledError):
            await task
        self.assertEqual(self.dispatcher.active, 0)

    async def test_restart_reuses_completed_step(self):
        with tempfile.TemporaryDirectory() as d:
            path = os.path.join(d, "journal.db")
            run = Run("persisted", "a")
            call = Call("1", "status", {"service": "db"})
            first = Journal(path)
            result = await Dispatcher(first).dispatch(run, call)
            first.close()
            second = Journal(path)
            try:
                dispatcher = Dispatcher(second)
                self.assertEqual(await dispatcher.dispatch(run, call), result)
                self.assertEqual(dispatcher.executions, 0)
                await dispatcher.dispatch(Run("persisted", "b"), call)
                self.assertEqual(dispatcher.executions, 1)
                with self.assertRaises(ValueError):
                    await dispatcher.dispatch(run, Call("1", "status", {"service": "api"}))
            finally:
                second.close()


if __name__ == "__main__":
    unittest.main()
