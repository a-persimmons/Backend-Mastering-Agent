# 实验基线

Python 3.11+，仅标准库。

```bash
python labs/runtime.py
python -m unittest discover -s labs -v
```

## 代码导览

- Call / Final：模型输出契约。
- FakeModel：确定性模拟，适合不花费 API 额度的测试。
- Dispatcher：只读工具 allowlist、参数校验、有界并发、超时。
- Journal：SQLite 已完成工具步骤记录，以 tenant/run/call 区分。
- Runtime：有限循环、全局 deadline 和可传播取消。
- Tests：正常执行、并发上限、步数预算、权限校验、取消、已完成步骤恢复。

## 重要边界

它并非完整 Agent Platform：没有 HTTP/SSE、持久化完整会话、分布式租约、真正的写操作授权、全局队列、真实模型和生产级沙盒。已完成步骤可重用，但工具执行与 journal 写入不是同一个外部事务；并发相同 call 可能重复只读查询。生产写操作必须由工具服务实现幂等协议，并解决外部成功而本地失败的窗口。

下一步按课程逐步实现：V0.2 API 与 RAG → V0.3 状态机及 context builder → V0.4 durable run 和有界队列 → V0.5 多租户与性能测试。实验应保存环境、失败样本、原始指标与 ADR。
