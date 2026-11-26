# Prompt 与结构化输出

::: tip 本课目标
把 Prompt 看作带概率性执行器的接口规范，而非安全边界。
:::

## 1. 原理与边界

系统指令定义任务和约束，用户输入是待处理的数据，工具结果是外部不可信内容。结构化输出需要明确 JSON Schema、必需字段和枚举；即使服务支持 schema 约束，也必须做业务校验与权限检查。Few-shot 要覆盖正常、异常和拒绝路径。

## 2. 贯穿项目中的例子

工单分类 schema: category 枚举 network/database/other，confidence 数值，evidence 数组。若用户输入要求忽略规则，不能改变 schema 或授权。低置信度是模型自评而非校准概率，需通过数据集验证阈值。

## 3. 动手实验

构建 20 条标注工单（含模糊、缺字段和注入样本）。比较无 schema、schema、schema+业务校验三组，记录有效 JSON 比例、分类准确率、误拒率。

先建立可运行基线，保存输入、日志、版本与失败样本，再进行对照实验。输出记录可采用[实验模板](../../guide.md)。

## 4. 验收标准

实现校验失败的明确错误与有界重试；解释 schema 合法但业务错误的反例。

## 5. 定向阅读

- [参考资料](https://platform.openai.com/docs/guides/structured-outputs)：JSON Schema、拒绝和不完整输出。

阅读后用自己的实现解释设计取舍，而不是抄写 API。
