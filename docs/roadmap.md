# 学习路线图

本课程假设读者已经具备 REST API、数据库、缓存、异步任务、测试与部署等后端基础。不会要求从机器学习数学或 Python 语法重新开始。

| 阶段 | 建议周期 | 能力产出 | 验收 |
| --- | --- | --- | --- |
| 1 基础认知 | 1–2 周 | 看得懂 | 不用框架完成工具调用循环 |
| 2 应用工程 | 3–4 周 | 做得出 | 可服务化、可评估的业务 Agent |
| 3 Core / Harness | 4–6 周 | 造得出 | 自己实现可测试执行引擎 |
| 4 Runtime / Platform | 6–8 周 | 扛得住 | 并发、恢复、配额与容量证据 |
| 5 高阶系统工程 | 持续 | 解得开 | 用实验解决未知问题 |

建议每周安排原理 25%、实现 45%、实验与复盘 30%。周期是估算，不是毕业条件；已经掌握的内容通过验收即可跳过。

## 后端能力如何迁移

| 后端能力 | Agent 对应问题 | 需要补齐 |
| --- | --- | --- |
| API 与 RPC | Tool Calling / MCP | 模型生成参数不可信 |
| 状态机、工作流 | Agent Loop / Runtime | 动态分支、终止与预算 |
| 数据库 | Session / Memory | 检索相关性、隐私与记忆冲突 |
| MQ 与任务调度 | Durable Execution | 长任务重试、外部副作用 |
| 监控与测试 | Tracing / Evals | 非确定性结果与轨迹质量 |
| 服务治理 | Model Gateway | Token 限额、供应商差异 |

## 课程目录

### 01 基础认知

- [模型与推理](./course/01-fundamentals/01-model.md)
- [模型 API 与流式输出](./course/01-fundamentals/02-api.md)
- [Prompt 与结构化输出](./course/01-fundamentals/03-prompt.md)
- [工具调用协议](./course/01-fundamentals/04-tools.md)
- [Agent Loop 与模式](./course/01-fundamentals/05-loop.md)

### 02 应用工程

- [框架与工作流](./course/02-application/01-framework.md)
- [RAG 与检索评估](./course/02-application/02-rag.md)
- [Context 与 Memory](./course/02-application/03-context.md)
- [MCP 与业务集成](./course/02-application/04-mcp.md)
- [服务化与 Evals](./course/02-application/05-delivery.md)

### 03 Core 与 Harness

- [状态机与事件模型](./course/03-core/01-state.md)
- [Tool Dispatcher 与安全](./course/03-core/02-tools.md)
- [上下文预算与压缩](./course/03-core/03-context.md)
- [长期记忆系统](./course/03-core/04-memory.md)
- [规划、反馈与 Harness](./course/03-core/05-harness.md)
- [成熟项目源码研读](./course/03-core/06-source.md)

### 04 Runtime 与 Platform

- [并发与流式通信](./course/04-runtime/01-concurrency.md)
- [调度与背压](./course/04-runtime/02-scheduling.md)
- [持久化执行与恢复](./course/04-runtime/03-durable.md)
- [模型网关与成本](./course/04-runtime/04-gateway.md)
- [沙盒与多租户](./course/04-runtime/05-security.md)
- [可观测性与 SLO](./course/04-runtime/06-observability.md)
- [压测与技术选型](./course/04-runtime/07-performance.md)
- [分布式部署与容量规划](./course/04-runtime/08-deploy.md)

### 05 复杂问题求解

- [问题求解方法](./course/05-advanced/01-method.md)
- [故障案例实验室](./course/05-advanced/02-incidents.md)
- [效果与性能优化](./course/05-advanced/03-optimization.md)
- [毕业项目与能力验收](./course/05-advanced/04-capstone.md)

## 取舍

Python 适合快速建立基线；Java、Go 可直接复用已有能力；Rust 按系统组件需要引入。不按语言预设性能结论。模型推理设施作为选修边界，不让 GPU 内核学习阻塞 Agent 主线。
