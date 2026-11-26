# 贯穿项目：企业工单 Agent

选择企业 IT 工单作为示例，因为它兼具知识检索、状态管理、工具调用、业务审批和真实副作用。后续可替换为 Coding Agent 或通用任务 Agent，而不必重写整个运行时。

## 需求与边界

输入自然语言工单，查询知识库、检查模拟服务状态、给出引用、必要时创建模拟工单。禁止自动执行真实生产变更；写操作需要明确审批和幂等键。

```text
Client → API / SSE → Agent Run → Model Adapter
                         ├→ Context / Memory
                         ├→ Tool Dispatcher → Mock IT API
                         └→ Events / Checkpoint / Evals
```

| 版本 | 对应课程 | 可验证交付 |
| --- | --- | --- |
| V0.1 | Stage 1 | CLI 工具循环，步数限制 |
| V0.2 | Stage 2 | 工单检索、引用、服务 API、评估集 |
| V0.3 | Stage 3 | 模型适配层、事件状态机、工具权限、上下文预算 |
| V0.4 | Stage 4 前半 | 有界队列、并发、取消、恢复 |
| V0.5 | Stage 4 后半 | 租户配额、追踪、网关、压测报告 |
| V1.0 | Stage 5 | 基于证据的架构决策和故障复盘 |

## 仓库中的实验起点

在仓库根目录执行：

```bash
python -m unittest discover -s labs -v
python labs/runtime.py
```

[实验代码目录](https://github.com/a-persimmons/Backend-Mastering-Agent/tree/main/labs) 使用 Python 标准库，模拟模型及工具，避免学习被 API 费用阻塞。它只是最小可验证基线，后续课程要求自行扩展数据库、真实模型、网关和分布式组件。

建议的数据结构：Run(id, tenant, status, deadline)、Event(run_id, seq, kind, payload)、ToolCall(id, name, arguments, idempotency_key)。Event 使用顺序号防止乱序，持久化后再通知客户端。

## 项目验收证据

提交架构图、API 契约、运行说明、测试集、评估报告、压测环境与原始数据、至少三次故障实验及两份 ADR。不要只交演示视频。所有真实密钥由环境变量读取；示例使用虚拟数据。
