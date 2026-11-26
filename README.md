# Backend Mastering Agent

**有经验的后端工程师转型 AI Agent 工程师的系统化课程。**

不是从零学习编程，也不是框架 API 大全。目标是从能够交付 Agent 应用，逐渐过渡到能够设计、实现、运行和优化 Agent 本体服务，最终独立处理陌生工程问题。

- [在线学习（部署后）](https://a-persimmons.github.io/Backend-Mastering-Agent/)
- [课程路线](docs/roadmap.md)
- [实践项目](docs/project.md)
- [学习与验收方法](docs/guide.md)
- [资料索引](docs/resources.md)

## 本地运行

需要 Node.js 22 或兼容版本、npm。

```bash
npm install
npm run docs:dev
npm run docs:build
```

## 实验代码

Python 3.11+，不需要模型 API Key：

```bash
python -m unittest discover -s labs -v
python labs/runtime.py
```

## 自动部署

在仓库 Settings → Pages → Build and deployment → Source 选择 GitHub Actions（首次配置）。之后每次推送 main 都会自动构建并部署；也可以在 Actions 手动运行 Deploy VitePress。

课程以中文为主，技术术语保留英文；代码为教学实现，不宣称已经过生产规模验证。实际模型实验需自行配置 API Key，禁止提交密钥。
