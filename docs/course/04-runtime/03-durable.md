# 持久化执行、幂等与故障恢复

::: tip 本课目标
长任务不能只存内存。重启后从已提交的状态恢复，但外部副作用仍须独立处理。
:::

## 1. 原理与边界

Checkpoint 是某时刻状态；事件日志提供 replay 和审计。步骤需有稳定 step_id、状态和尝试次数。任务领取采用 lease 或消息可见性超时，处理至少一次投递。事务 outbox 解决本地状态和消息发布双写；外部 API 仍需要幂等或补偿。Temporal workflow 需保持确定性，LLM 与外部 I/O 放在 activity。

## 2. 贯穿项目中的例子

写工单前持久化 step_id，使用供应商 idempotency_key。若写成功后进程崩溃，重启查询该键或安全重复请求，再提交结果；不要再次询问模型生成新的写操作。

## 3. 动手实验

执行 labs/test_runtime.py 中恢复测试；再设计进程在调用前、外部成功后、checkpoint 后三个时点崩溃的实验。对照 SQLite 原型与 Temporal cookbook，明确保证边界。

先记录基线、环境和失败样本，再做控制变量实验。使用[实验模板](../../guide.md)保存结论。

## 4. 验收标准

在模拟重启下已完成步骤不重复执行；至少一次投递的重复副作用测试通过；能解释外部系统不支持幂等时为什么不能承诺 exactly-once。

## 5. 定向阅读

- [参考资料](https://docs.temporal.io/ai/cookbook)：Durable agentic loop、tool activity、human-in-the-loop。

将阅读内容映射到自己的系统，明确哪些机制可以复用、哪些需要验证。
