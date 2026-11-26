# 分布式部署、容量与故障域

::: tip 本课目标
单体优先并不排斥扩展；先根据负载与故障边界拆分。
:::

## 1. 原理与边界

可将 API、scheduler、worker、model gateway、sandbox 分成逻辑组件，初期同进程或同部署，容量需要时再独立伸缩。会话和任务状态外置；worker drain 防止发布时丢任务，lease 过期可重领。队列积压、下游限额、并发 slots 共同决定扩容。HA 不仅是多个 pod，还包括存储、队列、依赖的故障域与恢复目标。

## 2. 贯穿项目中的例子

设计 API + worker + PostgreSQL + Redis/MQ 的初始架构。用户请求创建 run 后得到 id；worker 消费任务，提交事件，API SSE 重放。目标规模用假设标注，区分每秒新 run、在途 run、模型 RPM/TPM。

## 3. 动手实验

在本地容器或测试集群运行两个 worker，逐个停止、滚动更新、断开依赖，观察任务丢失/重复和恢复时间。设计 readiness、graceful shutdown、扩缩容与回滚。

先记录基线、环境和失败样本，再做控制变量实验。使用[实验模板](../../guide.md)保存结论。

## 4. 验收标准

V0.5 验收：有部署图、容量表、故障域和 RTO/RPO 假设；能复现 worker 故障并恢复；性能报告包含真实边界。

## 5. 定向阅读

- [参考资料](https://sre.google/sre-book/table-of-contents/)：Managing Critical State、Addressing Cascading Failures、Load Balancing。

将阅读内容映射到自己的系统，明确哪些机制可以复用、哪些需要验证。
