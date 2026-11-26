# 并发模型与流式通信

::: tip 本课目标
Agent 的并发不仅是请求 QPS，还包括长生命周期 run、模型流、工具 fan-out 和客户端订阅。
:::

## 1. 原理与边界

I/O 等待与 CPU 工作分开。Python asyncio 适合非阻塞 I/O，但同步 SDK、CPU 重任务会阻塞事件循环；Go goroutine、Java virtual threads 等也需要有界资源。每个外部依赖单独设 semaphore、连接池、deadline。SSE 慢客户端需要缓冲上限、断线重连与事件重放，而非无限积压。

## 2. 贯穿项目中的例子

100 个 run 同时各调用 3 个工具，不能直接无限 gather；限制模型并发 20、工具并发 10，取消时传播到下游。用 seq 恢复 SSE，客户端断线与任务取消不是同一个语义。

## 3. 动手实验

先用 labs/runtime.py 的 fake model 和工具比较无界与有界执行。再增加阻塞 sleep、慢消费者、取消；观察 event loop lag、在途数、P95、队列长度和 RSS。

先记录基线、环境和失败样本，再做控制变量实验。使用[实验模板](../../guide.md)保存结论。

## 4. 验收标准

展示并发上限的测试；取消后资源释放；解释 I/O 与 CPU 瓶颈的诊断证据。

## 5. 定向阅读

- [参考资料](https://docs.python.org/3/library/asyncio-task.html)：TaskGroup、取消、timeout、任务生命周期。

将阅读内容映射到自己的系统，明确哪些机制可以复用、哪些需要验证。
