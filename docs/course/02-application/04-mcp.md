# MCP、Skills 与业务集成

::: tip 本课目标
MCP 是连接工具和数据能力的协议，Skills 是可复用任务指导；二者并不自动解决权限和可靠性。
:::

## 1. 原理与边界

Host 管理 client 与用户交互，client 与 server 协商能力和工具。区分本地进程传输与远程 HTTP 传输；按规范版本选择。服务端鉴权、最小权限、超时和取消仍是业务责任。Skills 内容可被注入或失效，需要审阅和版本管理。

## 2. 贯穿项目中的例子

将模拟 IT 查询封装为 MCP tool，工具输出携带结构化状态和来源。写操作放在独立权限域，审批凭据由可信服务端持有。

## 3. 动手实验

接入一个只读 MCP server，模拟连接失败、工具列表变化、schema 演进和超时。记录调用链、退避策略和权限决策。

先建立可运行基线，保存输入、日志、版本与失败样本，再进行对照实验。输出记录可采用[实验模板](../../guide.md)。

## 4. 验收标准

能画出 Host/Client/Server 与工具执行边界；对异常 server 有失败策略；未经批准不能写。

## 5. 定向阅读

- [参考资料](https://modelcontextprotocol.io/specification/)：Architecture、Lifecycle、Tools、Authorization。

阅读后用自己的实现解释设计取舍，而不是抄写 API。
