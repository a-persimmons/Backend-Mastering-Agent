# Agent 状态机与事件模型

::: tip 本课目标
执行引擎的核心不是 while true，而是可解释、可观察、可恢复的状态转换。
:::

## 1. 原理与边界

Run 状态可设计为 QUEUED/RUNNING/WAITING_APPROVAL/SUCCEEDED/FAILED/CANCELLED。终态不可逆。每个事件带 run_id、seq、timestamp、kind、schema_version；状态通过事件折叠。并发写入使用事务、唯一约束和版本检查。事件先持久化再发布；客户端按 seq 去重。

## 2. 贯穿项目中的例子

模型提议工具调用后，先写 ToolRequested，再检查权限；写操作需要 ApprovalGranted，执行后 ToolCompleted，最后 RunSucceeded。不能因为 SSE 丢包而改变数据库状态。

## 3. 动手实验

画状态转换表，编写纯函数 reduce(state,event)，测试非法转换和重复事件。模拟 seq=4 比 seq=3 先抵达客户端。

先建立可运行基线，保存输入、日志、版本与失败样本，再进行对照实验。输出记录可采用[实验模板](../../guide.md)。

## 4. 验收标准

实现状态投影和 replay 测试；说明事件日志、checkpoint 与用户可见消息的区别。

## 5. 定向阅读

- [参考资料](https://github.com/openai/codex)：从 codex-rs 中寻找会话、事件与运行循环入口。

阅读后用自己的实现解释设计取舍，而不是抄写 API。
