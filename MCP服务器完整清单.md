# MCP服务器完整清单

**数据来源**: https://github.com/modelcontextprotocol/servers
**提取日期**: 2026-01-18
**总计**: 1442+ 个MCP服务器

---

## 📊 概览

| 类别 | 数量 | 说明 |
|-----|------|------|
| 参考服务器 | 7 | 由MCP指导小组维护的官方示例服务器 |
| 已归档服务器 | 13 | 已归档的参考服务器，可在servers-archived仓库找到 |
| 第三方服务器 | 1422+ | 社区和公司构建的生产就绪MCP服务器 |
| **总计** | **1442+** | **所有可用的MCP服务器** |

---

## 🌟 一、参考服务器 (Reference Servers)

由MCP指导小组维护，用于演示MCP功能和官方SDK。

| # | 名称 | 功能描述 | GitHub链接 |
|---|------|----------|------------|
| 1 | **Everything** | 参考/测试服务器，包含prompts、resources和tools | [查看](https://github.com/modelcontextprotocol/servers/tree/main/src/everything) |
| 2 | **Fetch** | 网页内容获取和转换，用于高效的LLM使用 | [查看](https://github.com/modelcontextprotocol/servers/tree/main/src/fetch) |
| 3 | **Filesystem** | 具有可配置访问控制的安全文件操作 | [查看](https://github.com/modelcontextprotocol/servers/tree/main/src/filesystem) |
| 4 | **Git** | 读取、搜索和操作Git仓库的工具 | [查看](https://github.com/modelcontextprotocol/servers/tree/main/src/git) |
| 5 | **Memory** | 基于知识图谱的持久化内存系统 | [查看](https://github.com/modelcontextprotocol/servers/tree/main/src/memory) |
| 6 | **Sequential Thinking** | 通过思维序列进行动态和反思性问题解决 | [查看](https://github.com/modelcontextprotocol/servers/tree/main/src/sequential-thinking) |
| 7 | **Time** | 时间和时区转换功能 | [查看](https://github.com/modelcontextprotocol/servers/tree/main/src/time) |

### 安装参考服务器

参考服务器通常可以通过以下方式安装：

```bash
# 克隆仓库
git clone https://github.com/modelcontextprotocol/servers.git
cd servers

# 进入特定服务器目录
cd src/[server-name]

# 根据README安装和运行
npm install  # 或其他包管理器
npm start
```

---

## 📦 二、已归档服务器 (Archived Servers)

这些参考服务器现已归档，可在 https://github.com/modelcontextprotocol/servers-archived 找到。

| # | 名称 | 功能描述 | 归档仓库 |
|---|------|----------|----------|
| 1 | **AWS KB Retrieval** | 使用Bedrock Agent Runtime从AWS知识库检索 | [查看](https://github.com/modelcontextprotocol/servers-archived) |
| 2 | **Brave Search** | 使用Brave搜索API进行网页和本地搜索（已被官方服务器替代） | [查看](https://github.com/modelcontextprotocol/servers-archived) |
| 3 | **EverArt** | 使用各种模型进行AI图像生成 | [查看](https://github.com/modelcontextprotocol/servers-archived) |
| 4 | **GitHub** | 仓库管理、文件操作和GitHub API集成 | [查看](https://github.com/modelcontextprotocol/servers-archived) |
| 5 | **GitLab** | GitLab API，实现项目管理 | [查看](https://github.com/modelcontextprotocol/servers-archived) |
| 6 | **Google Drive** | Google Drive的文件访问和搜索功能 | [查看](https://github.com/modelcontextprotocol/servers-archived) |
| 7 | **Google Maps** | 位置服务、导航和地点详情 | [查看](https://github.com/modelcontextprotocol/servers-archived) |
| 8 | **PostgreSQL** | 只读数据库访问和架构检查 | [查看](https://github.com/modelcontextprotocol/servers-archived) |
| 9 | **Puppeteer** | 浏览器自动化和网页抓取 | [查看](https://github.com/modelcontextprotocol/servers-archived) |
| 10 | **Redis** | 与Redis键值存储交互 | [查看](https://github.com/modelcontextprotocol/servers-archived) |
| 11 | **Sentry** | 从Sentry.io检索和分析问题 | [查看](https://github.com/modelcontextprotocol/servers-archived) |
| 12 | **Slack** | 频道管理和消息功能（现由Zencoder维护） | [查看](https://github.com/modelcontextprotocol/servers-archived) |
| 13 | **SQLite** | 数据库交互和商业智能功能 | [查看](https://github.com/modelcontextprotocol/servers-archived) |

---

## 🤝 三、第三方服务器 (Third-Party Servers)

> **重要提示**: README中的服务器列表不再主动维护。建议访问 [MCP Registry](https://registry.mcp.io/) 获取最新的服务器列表。

### 分类统计

第三方服务器涵盖以下主要类别：

| 类别 | 示例服务器 | 数量估计 |
|------|-----------|---------|
| **云平台** | AWS, Azure, Google Cloud, Alibaba Cloud, Cloudflare | 50+ |
| **数据库** | PostgreSQL, MySQL, MongoDB, Redis, Snowflake, ClickHouse | 80+ |
| **开发工具** | GitHub, GitLab, CircleCI, Buildkite, Jenkins | 100+ |
| **AI/ML** | OpenAI, Anthropic, Hugging Face, LangChain, Ollama | 60+ |
| **支付系统** | Stripe, PayPal, Cashfree, Alipay, Square | 40+ |
| **通信** | Slack, Discord, Telegram, WhatsApp, Teams | 50+ |
| **CRM** | Salesforce, HubSpot, Zendesk, Intercom | 30+ |
| **项目管理** | Jira, Asana, Linear, Notion, Monday | 40+ |
| **电商** | Shopify, WooCommerce, Magento, BigCommerce | 30+ |
| **监控** | Datadog, Sentry, Axiom, New Relic | 35+ |
| **其他** | 各种专业领域服务器 | 900+ |

### 热门第三方服务器

#### 云平台与基础设施

1. **AWS** - 将AWS最佳实践直接带到您的开发工作流程的专业MCP服务器
2. **Azure** - 提供对Azure Storage、Cosmos DB、Azure CLI等关键Azure服务的访问
3. **Google Cloud Platform** - 与GCP服务交互
4. **Cloudflare** - 部署、配置和查询Cloudflare开发者平台资源
5. **Alibaba Cloud** - 多个专业服务器（RDS、AnalyticDB、DataWorks、OpenSearch等）

#### 数据库

6. **PostgreSQL** - 数据库查询和管理
7. **MySQL** - MySQL数据库操作
8. **MongoDB** - NoSQL数据库交互
9. **Redis** - 键值存储操作
10. **Snowflake** - 数据仓库查询和分析
11. **ClickHouse** - 实时分析数据库
12. **Apache Doris** - MPP实时数据仓库
13. **Astra DB** - DataStax NoSQL数据库管理

#### 开发工具

14. **GitHub** - 仓库管理、PR、Issues等
15. **GitLab** - 项目管理和CI/CD
16. **CircleCI** - 修复构建失败
17. **Buildkite** - 管道、构建、作业数据
18. **Jenkins/CloudBees CI** - 企业级CI/CD
19. **Bitrise** - 移动CI/CD
20. **Azure DevOps** - 完整的DevOps工具链

#### AI与机器学习

21. **OpenAI** - GPT模型集成
22. **Anthropic** - Claude模型访问
23. **Hugging Face** - 模型托管和推理
24. **LangChain** - LLM应用开发框架
25. **Ollama** - 本地LLM运行
26. **Arize Phoenix** - AI可观察性
27. **Chronulus AI** - 预测和预测代理

#### 支付与金融

28. **Stripe** - 在线支付处理
29. **PayPal** - 支付集成
30. **Cashfree** - 印度支付解决方案
31. **Alipay Plus** - 支付宝国际版
32. **Square** - 支付和商务平台
33. **Bitnovo Pay** - 加密货币支付
34. **CoinGecko** - 加密货币市场数据

#### 通信与协作

35. **Slack** - 频道管理和消息
36. **Discord** - 社区管理
37. **Telegram** - 消息机器人
38. **Microsoft Teams** - 企业协作
39. **Zoom** - 视频会议管理
40. **Twilio** - 短信和语音API

#### CRM与客户服务

41. **Salesforce** - 客户关系管理
42. **HubSpot** - 营销和销售平台
43. **Zendesk** - 客户支持
44. **Intercom** - 客户消息平台
45. **Freshdesk** - 帮助台软件

#### 项目管理

46. **Jira** - 问题跟踪和项目管理
47. **Asana** - 团队协作和任务管理
48. **Linear** - 问题跟踪
49. **Notion** - 知识管理和协作
50. **Monday.com** - 工作操作系统
51. **Atono** - 产品团队管理

#### 电商平台

52. **Shopify** - 电子商务平台
53. **WooCommerce** - WordPress电商插件
54. **Magento** - 开源电商平台
55. **BigCommerce** - SaaS电商解决方案

#### 监控与可观察性

56. **Datadog** - 基础设施和应用监控
57. **Sentry** - 错误跟踪和性能监控
58. **Axiom** - 日志和事件数据分析
59. **New Relic** - 应用性能监控
60. **Arize Phoenix** - AI可观察性

#### 内容与媒体

61. **Cloudinary** - 媒体管理和优化
62. **Canva** - 设计平台API
63. **YouTube** - 视频平台集成
64. **Spotify** - 音乐流媒体API
65. **Unsplash** - 免费图片库

#### 搜索与数据

66. **Algolia** - 搜索即服务
67. **Elasticsearch** - 搜索和分析引擎
68. **Brave Search** - 隐私优先搜索
69. **Exa** - AI搜索API
70. **Perplexity** - AI搜索引擎

#### 安全与合规

71. **BoostSecurity** - 依赖安全扫描
72. **Snyk** - 安全漏洞检测
73. **Auth0** - 身份验证和授权
74. **Okta** - 身份管理
75. **CrowdStrike Falcon** - 安全平台

#### 测试与质量保证

76. **BrowserStack** - 跨浏览器测试
77. **Selenium** - Web自动化测试
78. **Playwright** - 浏览器自动化
79. **Appium** - 移动自动化测试
80. **AltTester** - Unity/Unreal游戏测试

#### 数据分析与BI

81. **Tableau** - 数据可视化
82. **Power BI** - 商业智能
83. **Looker** - 数据探索平台
84. **Metabase** - 开源BI工具
85. **Amplitude** - 产品分析

#### 营销与SEO

86. **Google Analytics** - 网站分析
87. **SEMrush** - SEO和营销工具
88. **Mailchimp** - 邮件营销
89. **SendGrid** - 邮件发送服务
90. **HubSpot Marketing** - 营销自动化

#### 文档与知识管理

91. **Confluence** - 团队协作和文档
92. **Notion** - 多功能工作空间
93. **Archbee** - 文档平台
94. **GitBook** - 文档创作工具
95. **ReadMe** - API文档平台

#### 区块链与Web3

96. **Ethereum** - 以太坊区块链交互
97. **Solana** - Solana区块链
98. **Polygon** - Layer 2扩展方案
99. **Armor Crypto** - 多链DeFi操作
100. **Cheqd** - 去中心化身份验证

### 完整的第三方服务器列表

完整的1422+个第三方服务器详细列表请查看：**所有第三方MCP服务器.md** 文件

该文件包含每个服务器的：
- 服务器名称
- 详细功能描述
- 按字母顺序排列

---

## 🛠️ MCP SDK支持

MCP提供10种编程语言的官方SDK：

| 语言 | SDK仓库 | 适用场景 |
|------|---------|---------|
| **TypeScript** | [typescript-sdk](https://github.com/modelcontextprotocol/typescript-sdk) | Web应用、Node.js服务 |
| **Python** | [python-sdk](https://github.com/modelcontextprotocol/python-sdk) | AI/ML应用、数据科学 |
| **Go** | [go-sdk](https://github.com/modelcontextprotocol/go-sdk) | 高性能服务、云原生应用 |
| **Rust** | [rust-sdk](https://github.com/modelcontextprotocol/rust-sdk) | 系统编程、高性能计算 |
| **Java** | [java-sdk](https://github.com/modelcontextprotocol/java-sdk) | 企业应用、Android开发 |
| **Kotlin** | [kotlin-sdk](https://github.com/modelcontextprotocol/kotlin-sdk) | Android应用、服务端开发 |
| **C#** | [csharp-sdk](https://github.com/modelcontextprotocol/csharp-sdk) | .NET应用、Unity游戏 |
| **Swift** | [swift-sdk](https://github.com/modelcontextprotocol/swift-sdk) | iOS/macOS应用开发 |
| **Ruby** | [ruby-sdk](https://github.com/modelcontextprotocol/ruby-sdk) | Web应用、脚本自动化 |
| **PHP** | [php-sdk](https://github.com/modelcontextprotocol/php-sdk) | Web应用、WordPress插件 |

---

## 📚 快速开始指南

### 1. 安装MCP客户端

```bash
# 使用Claude Desktop（推荐）
# 下载地址：https://claude.ai/download

# 或使用其他MCP客户端
npm install -g @modelcontextprotocol/client
```

### 2. 配置MCP服务器

在Claude Desktop配置文件中添加服务器：

**Windows**: `%APPDATA%\Claude\claude_desktop_config.json`
**macOS**: `~/Library/Application Support/Claude/claude_desktop_config.json`

```json
{
  "mcpServers": {
    "filesystem": {
      "command": "npx",
      "args": [
        "-y",
        "@modelcontextprotocol/server-filesystem",
        "/path/to/allowed/directory"
      ]
    },
    "github": {
      "command": "npx",
      "args": [
        "-y",
        "@modelcontextprotocol/server-github"
      ],
      "env": {
        "GITHUB_TOKEN": "your-token-here"
      }
    }
  }
}
```

### 3. 重启客户端

重启Claude Desktop以加载配置的MCP服务器。

---

## 🔗 重要资源

| 资源 | 链接 | 描述 |
|------|------|------|
| **MCP Registry** | https://registry.mcp.io/ | 官方MCP服务器注册表 |
| **官方文档** | https://modelcontextprotocol.io/ | MCP协议文档 |
| **GitHub主仓库** | https://github.com/modelcontextprotocol/servers | 参考服务器源代码 |
| **归档仓库** | https://github.com/modelcontextprotocol/servers-archived | 已归档的服务器 |
| **社区论坛** | https://reddit.com/r/modelcontextprotocol | Reddit社区讨论 |
| **Discord** | https://discord.gg/modelcontextprotocol | 实时社区支持 |

---

## 📝 使用建议

### 选择合适的服务器

1. **参考服务器**: 适合学习MCP协议和SDK使用
2. **官方集成**: 生产环境使用，由公司官方维护
3. **社区服务器**: 快速原型开发，但需评估维护状况

### 安全考虑

- 仅使用可信来源的MCP服务器
- 检查服务器权限和访问范围
- 定期更新服务器到最新版本
- 使用环境变量管理敏感信息
- 在生产环境前进行充分测试

### 性能优化

- 只启用必要的MCP服务器
- 配置合理的超时时间
- 监控服务器资源使用
- 使用缓存减少API调用

---

## 🎯 常见用例

### 开发工作流

- **代码管理**: GitHub, GitLab
- **CI/CD**: CircleCI, Jenkins, GitHub Actions
- **问题跟踪**: Jira, Linear, Asana
- **文档**: Notion, Confluence, Archbee

### 数据工作流

- **数据仓库**: Snowflake, BigQuery, Redshift
- **数据库**: PostgreSQL, MySQL, MongoDB
- **分析**: Tableau, Metabase, Amplitude
- **搜索**: Elasticsearch, Algolia, Meilisearch

### AI工作流

- **LLM**: OpenAI, Anthropic, Ollama
- **向量数据库**: Pinecone, Weaviate, Chroma
- **监控**: Arize Phoenix, Opik
- **RAG**: LangChain, LlamaIndex

### 业务工作流

- **CRM**: Salesforce, HubSpot
- **支付**: Stripe, PayPal
- **电商**: Shopify, WooCommerce
- **营销**: Mailchimp, SendGrid

---

## 🚀 贡献指南

### 创建自己的MCP服务器

1. 选择合适的SDK（推荐TypeScript或Python）
2. 实现MCP协议规范
3. 添加必要的工具、资源和提示
4. 编写文档和使用示例
5. 发布到npm/PyPI
6. 提交到MCP Registry

### 提交到官方仓库

1. Fork官方仓库
2. 创建feature分支
3. 添加服务器到README
4. 提交Pull Request
5. 等待审核和合并

---

## ⚠️ 重要说明

1. **README列表已停止维护**: GitHub仓库的README中的第三方服务器列表将不再更新
2. **使用MCP Registry**: 建议访问 https://registry.mcp.io/ 获取最新服务器列表
3. **版本兼容性**: 确保MCP服务器版本与客户端兼容
4. **安全审查**: 使用第三方服务器前进行安全审查
5. **许可证**: 检查服务器的开源许可证

---

## 📊 统计信息

- **参考服务器**: 7个（官方维护）
- **已归档服务器**: 13个（不再维护）
- **第三方服务器**: 1422+个（持续增长）
- **支持的SDK**: 10种编程语言
- **覆盖领域**: 云平台、数据库、开发工具、AI/ML、支付、通信等20+个领域

---

**文档版本**: 1.0
**最后更新**: 2026-01-18
**数据来源**: https://github.com/modelcontextprotocol/servers
**生成工具**: Claude Code

---

## 附录文件

本次提取生成了以下文件：

1. **MCP服务器完整列表.md** - 本文件，包含概览和分类信息
2. **所有第三方MCP服务器.md** - 完整的1422+个第三方服务器详细列表
3. **mcp_servers_list.txt** - 原始提取的文本数据

所有文件保存在：`C:\Users\admin\Desktop\自动运行skill\`
