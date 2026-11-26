# Agent 服务化与 Evals

::: tip 本课目标
交付不仅是 REST 接口能返回 200，还要证明任务成功、引用正确和风险可控。
:::

## 1. 原理与边界

API 建议 POST /runs 创建任务，GET /runs/{id} 查询，GET /runs/{id}/events 流式消费，POST /runs/{id}/cancel 取消。模型错误不等于 HTTP 错误；持久化终态。Evals 包含结果和轨迹：工具是否正确、调用是否越权、成本是否合理。人工标签与确定性断言优先，LLM judge 需校准。

## 2. 贯穿项目中的例子

构造 50 条工单样本，包含正常诊断、无答案、错误工具、审批拒绝。指标：task_success、citation_accuracy、unsafe_action、平均 token 与 P95。以固定版本为基线。

## 3. 动手实验

用 FastAPI 或 Spring Boot 暴露上述接口；在 CI 跑 deterministic fake 的回归集，再用少量真实模型做评估，报告样本数量与方差。

先建立可运行基线，保存输入、日志、版本与失败样本，再进行对照实验。输出记录可采用[实验模板](../../guide.md)。

## 4. 验收标准

V0.2 验收：API、流式事件、取消或明确不支持的边界；至少 30 条评估，且未授权写入为零。

## 5. 定向阅读

- [参考资料](https://openai.github.io/openai-agents-python/tracing/)：Tracing、span 与敏感数据控制。

阅读后用自己的实现解释设计取舍，而不是抄写 API。
