import { defineConfig } from 'vitepress'

export default defineConfig({
  lang: 'zh-CN',
  title: 'Backend Mastering Agent',
  description: '从后端工程师到生产级 Agent 系统工程师',
  base: '/Backend-Mastering-Agent/',
  cleanUrls: false,
  lastUpdated: true,
  themeConfig: {
    nav: [
      { text: '路线图', link: '/roadmap' },
      { text: '开始学习', link: '/course/01-fundamentals/01-model' },
      { text: '实践项目', link: '/project' },
      { text: '学习方法', link: '/guide' },
      { text: '资料', link: '/resources' }
    ],
    sidebar: [
  {
    "text": "学习指南",
    "items": [
      {
        "text": "路线图",
        "link": "/roadmap"
      },
      {
        "text": "学习方法",
        "link": "/guide"
      },
      {
        "text": "贯穿项目",
        "link": "/project"
      },
      {
        "text": "资料索引",
        "link": "/resources"
      }
    ]
  },
  {
    "text": "01 基础认知",
    "collapsed": false,
    "items": [
      {
        "text": "模型与推理",
        "link": "/course/01-fundamentals/01-model"
      },
      {
        "text": "模型 API 与流式输出",
        "link": "/course/01-fundamentals/02-api"
      },
      {
        "text": "Prompt 与结构化输出",
        "link": "/course/01-fundamentals/03-prompt"
      },
      {
        "text": "工具调用协议",
        "link": "/course/01-fundamentals/04-tools"
      },
      {
        "text": "Agent Loop 与模式",
        "link": "/course/01-fundamentals/05-loop"
      }
    ]
  },
  {
    "text": "02 应用工程",
    "collapsed": false,
    "items": [
      {
        "text": "框架与工作流",
        "link": "/course/02-application/01-framework"
      },
      {
        "text": "RAG 与检索评估",
        "link": "/course/02-application/02-rag"
      },
      {
        "text": "Context 与 Memory",
        "link": "/course/02-application/03-context"
      },
      {
        "text": "MCP 与业务集成",
        "link": "/course/02-application/04-mcp"
      },
      {
        "text": "服务化与 Evals",
        "link": "/course/02-application/05-delivery"
      }
    ]
  },
  {
    "text": "03 Core 与 Harness",
    "collapsed": false,
    "items": [
      {
        "text": "状态机与事件模型",
        "link": "/course/03-core/01-state"
      },
      {
        "text": "Tool Dispatcher 与安全",
        "link": "/course/03-core/02-tools"
      },
      {
        "text": "上下文预算与压缩",
        "link": "/course/03-core/03-context"
      },
      {
        "text": "长期记忆系统",
        "link": "/course/03-core/04-memory"
      },
      {
        "text": "规划、反馈与 Harness",
        "link": "/course/03-core/05-harness"
      },
      {
        "text": "成熟项目源码研读",
        "link": "/course/03-core/06-source"
      }
    ]
  },
  {
    "text": "04 Runtime 与 Platform",
    "collapsed": false,
    "items": [
      {
        "text": "并发与流式通信",
        "link": "/course/04-runtime/01-concurrency"
      },
      {
        "text": "调度与背压",
        "link": "/course/04-runtime/02-scheduling"
      },
      {
        "text": "持久化执行与恢复",
        "link": "/course/04-runtime/03-durable"
      },
      {
        "text": "模型网关与成本",
        "link": "/course/04-runtime/04-gateway"
      },
      {
        "text": "沙盒与多租户",
        "link": "/course/04-runtime/05-security"
      },
      {
        "text": "可观测性与 SLO",
        "link": "/course/04-runtime/06-observability"
      },
      {
        "text": "压测与技术选型",
        "link": "/course/04-runtime/07-performance"
      },
      {
        "text": "分布式部署与容量规划",
        "link": "/course/04-runtime/08-deploy"
      }
    ]
  },
  {
    "text": "05 复杂问题求解",
    "collapsed": false,
    "items": [
      {
        "text": "问题求解方法",
        "link": "/course/05-advanced/01-method"
      },
      {
        "text": "故障案例实验室",
        "link": "/course/05-advanced/02-incidents"
      },
      {
        "text": "效果与性能优化",
        "link": "/course/05-advanced/03-optimization"
      },
      {
        "text": "毕业项目与能力验收",
        "link": "/course/05-advanced/04-capstone"
      }
    ]
  }
],
    outline: { level: [2, 3], label: '本页目录' },
    search: { provider: 'local' },
    socialLinks: [{ icon: 'github', link: 'https://github.com/a-persimmons/Backend-Mastering-Agent' }],
    docFooter: { prev: '上一课', next: '下一课' },
    lastUpdated: { text: '更新于' },
    sidebarMenuLabel: '课程目录',
    returnToTopLabel: '返回顶部',
    darkModeSwitchLabel: '外观',
    footer: { message: '从理解机制到独立解决问题', copyright: 'Backend Mastering Agent' }
  }
})
