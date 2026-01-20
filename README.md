# 🔥 微博热搜产品创意自动分析系统

[![GitHub Actions](https://img.shields.io/badge/GitHub-Actions-2088FF?logo=github-actions&logoColor=white)](https://github.com/features/actions)
[![Claude API](https://img.shields.io/badge/Claude-API-7C3AED?logo=anthropic&logoColor=white)](https://www.anthropic.com/)
[![Python 3.11+](https://img.shields.io/badge/Python-3.11+-3776AB?logo=python&logoColor=white)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

基于 **Claude Agent SDK** 和 **GitHub Actions** 的微博热搜自动分析与产品创意生成系统。每天自动抓取微博热搜，使用 AI 深度分析并生成可行的产品创意方案。

---

## ✨ 功能特性

- 🤖 **AI 驱动分析** - 使用 Claude 3.5 Sonnet 进行深度热点分析
- 📊 **智能评分** - 80% 有趣度 + 20% 有用度的双维度评分模型
- 💡 **产品创意生成** - 为每个热点生成 1-3 个可行的产品创意
- ⏰ **定时自动运行** - GitHub Actions 定时触发，无需服务器
- 📈 **精美报告** - 自动生成响应式 HTML 可视化报告
- 🔒 **安全可靠** - 使用 GitHub Secrets 管理 API 密钥
- 📦 **开箱即用** - 完整配置，fork 即可使用

---

## 🎯 使用场景

### 适合人群

- 📱 **产品经理** - 快速发现市场机会和产品方向
- 🚀 **创业者** - 从热点趋势中挖掘创业想法
- ✍️ **内容创作者** - 了解热点趋势，创作更有影响力的内容
- 📊 **市场研究人员** - 分析社交媒体趋势，生成研究报告
- 💼 **投资人** - 识别新兴市场和投资机会

### 典型场景

```
每日早晨 10:00 → 自动获取微博热搜
              ↓
         AI 深度分析（背景研究 + 事件时间线）
              ↓
         生成产品创意（评分 + 可行性分析）
              ↓
         生成 HTML 报告并发送通知
```

---

## 🚀 快速开始

### 前置要求

1. **GitHub 账号**
2. **Anthropic API Key** - [获取地址](https://console.anthropic.com/)
3. **TianAPI Key**（可选）- [获取地址](https://www.tianapi.com/)，有默认密钥可用

### 一键部署（3 分钟）

#### 步骤 1: Fork 本仓库

点击右上角 **Fork** 按钮，复制到你的 GitHub 账号。

#### 步骤 2: 配置 Secrets

在你的仓库中：

1. 进入 `Settings` → `Secrets and variables` → `Actions`
2. 添加以下 Secrets：

| Secret Name | 说明 | 如何获取 |
|------------|------|---------|
| `ANTHROPIC_API_KEY` | Claude API 密钥 | [Anthropic Console](https://console.anthropic.com/) |
| `TIANAPI_KEY` | 微博热搜 API 密钥 | 使用默认: `eda7b8c9c35234ce9a0dfd6939ae8c85`<br>或[申请自己的](https://www.tianapi.com/) |

#### 步骤 3: 手动触发首次运行

1. 进入 `Actions` 标签
2. 选择 **Weibo Trending Analysis**
3. 点击 `Run workflow` → `Run workflow`
4. 等待 1-2 分钟，查看结果

#### 步骤 4: 下载分析报告

运行完成后：
- 滚动到 **Artifacts** 部分
- 下载 `weibo-analysis-report-xxx`
- 解压并在浏览器中打开 HTML 文件

🎉 **完成！** 你的自动化分析系统已经开始工作了！

---

## 📊 报告示例

### 报告内容

每份报告包含：

```
📊 统计概览
├─ 分析热点数量: 15
├─ 优秀创意 (≥80分): 3 个
├─ 良好创意 (60-79分): 8 个
└─ 产品创意总数: 28 个

🏆 热点分析（按评分排序）
├─ #1 话题标题
│   ├─ 📅 事件时间线
│   ├─ 🔍 背景分析
│   ├─ 💡 产品创意 1-3 个
│   │   ├─ 产品名称
│   │   ├─ 核心功能
│   │   ├─ 目标用户
│   │   ├─ 创新角度
│   │   └─ 评分明细
│   └─ ⭐ 综合评分: 86/100
├─ #2 话题标题 ...
└─ ...
```

### 评分模型

**有趣度（80分）**
- 病毒传播潜力（0-20分）
- 情感吸引力（0-20分）
- 社区参与度（0-20分）
- 文化相关性（0-20分）

**有用度（20分）**
- 问题解决潜力（0-10分）
- 市场需求（0-10分）

**综合评分 = 有趣度 + 有用度**

---

## ⚙️ 配置说明

### 定时运行设置

编辑 `.github/workflows/weibo-analysis.yml`:

```yaml
schedule:
  # 每天北京时间 10:00 (UTC 2:00)
  - cron: '0 2 * * *'

  # 每 6 小时一次
  # - cron: '0 */6 * * *'

  # 每周一早上 9:00 (UTC 1:00)
  # - cron: '0 1 * * 1'
```

### 分析参数调整

编辑 `scripts/weibo_analysis_agent.py`:

```python
MAX_TOPICS = 15              # 分析热点数量（建议 10-20）
MIN_SCORE_EXCELLENT = 80     # 优秀创意标准
MIN_SCORE_GOOD = 60          # 良好创意标准
```

或在 workflow 中手动触发时修改 `max_topics` 参数。

---

## 📁 项目结构

```
.
├── .github/
│   └── workflows/
│       └── weibo-analysis.yml          # GitHub Actions 工作流
├── scripts/
│   ├── weibo_analysis_agent.py         # 主分析脚本（Claude SDK）
│   └── requirements.txt                # Python 依赖
├── reports/                            # 生成的报告（自动创建）
├── .claude/                            # 原 Claude Code Skill 配置
│   └── skills/
│       └── weibo-trending-product-ideas/
├── .gitignore
├── DEPLOYMENT_GUIDE.md                 # 详细部署指南
├── SECRETS_SETUP.md                    # Secrets 配置说明
└── README.md                           # 本文档
```

---

## 🔧 技术架构

```
┌──────────────────────────────────────────────────────┐
│                  GitHub Actions                       │
│  ┌────────────────────────────────────────────────┐  │
│  │  Cron Scheduler (定时触发)                     │  │
│  └──────────────────┬─────────────────────────────┘  │
│                     ↓                                 │
│  ┌────────────────────────────────────────────────┐  │
│  │  Step 1: 获取微博热搜                          │  │
│  │  • API: TianAPI Weibo Hot Search               │  │
│  │  • 数据: 热点标题 + 热度值                      │  │
│  └──────────────────┬─────────────────────────────┘  │
│                     ↓                                 │
│  ┌────────────────────────────────────────────────┐  │
│  │  Step 2: Claude AI 深度分析                    │  │
│  │  • SDK: Anthropic Python SDK                   │  │
│  │  • Model: Claude 3.5 Sonnet                    │  │
│  │  • 输出: JSON 结构化数据                        │  │
│  └──────────────────┬─────────────────────────────┘  │
│                     ↓                                 │
│  ┌────────────────────────────────────────────────┐  │
│  │  Step 3: 生成 HTML 报告                        │  │
│  │  • 模板: 响应式设计                             │  │
│  │  • 样式: 分级高亮显示                           │  │
│  └──────────────────┬─────────────────────────────┘  │
│                     ↓                                 │
│  ┌────────────────────────────────────────────────┐  │
│  │  Outputs                                       │  │
│  │  • Artifact 下载                                │  │
│  │  • Git 提交（可选）                             │  │
│  │  • Summary 展示                                 │  │
│  └────────────────────────────────────────────────┘  │
└──────────────────────────────────────────────────────┘
```

---

## 💰 成本估算

### Claude API 费用

**Claude 3.5 Sonnet 定价**:
- Input: $3.00 / 1M tokens
- Output: $15.00 / 1M tokens

**单次分析成本**:
- 约 5,000-8,000 input tokens
- 约 8,000-12,000 output tokens
- **成本: ~$0.10 - 0.30 USD/次**

**每月成本**（每天运行 1 次）:
- 30 次 × $0.20 = **~$6 USD/月**

### TianAPI 费用

- **免费额度**: 100 次/天（完全免费）
- **付费版**: 更高额度

### 总计

**每月总成本: ~$6-10 USD**（适合个人和小团队使用）

---

## 📚 文档

- 📖 **[部署指南](./DEPLOYMENT_GUIDE.md)** - 完整的一步步部署教程
- 🔐 **[Secrets 配置](./SECRETS_SETUP.md)** - API 密钥获取和配置说明
- 💡 **[原 Skill 文档](./.claude/skills/weibo-trending-product-ideas/README.md)** - Claude Code Skill 版本

---

## 🐛 故障排查

### 问题 1: Workflow 未自动运行

**解决方案**:
- 检查 Actions 是否启用（Settings → Actions）
- 手动触发一次激活定时任务
- 确认仓库有最近的活动

### 问题 2: API 调用失败

**检查清单**:
- ✅ Secrets 配置正确
- ✅ API 密钥有效
- ✅ 账户余额充足
- ✅ 网络连接正常

**调试方法**:
查看 Actions 运行日志，定位具体错误。

### 问题 3: 报告内容为空

**可能原因**:
- TianAPI 返回数据为空
- Claude API 响应解析失败

**解决方案**:
1. 检查 workflow 日志
2. 手动测试 TianAPI:
   ```bash
   curl "https://apis.tianapi.com/weibohot/index?key=YOUR_KEY"
   ```

更多问题参见 [部署指南](./DEPLOYMENT_GUIDE.md#常见问题)。

---

## 🤝 贡献

欢迎提交 Issue 和 Pull Request！

### 改进建议

- 💡 添加更多数据源（抖音热点、知乎热榜等）
- 📧 集成邮件/Slack/微信通知
- 📊 数据可视化增强（图表、趋势分析）
- 🌍 多语言支持
- 🗄️ 数据持久化（数据库存储）

---

## 📄 许可证

本项目采用 [MIT License](https://opensource.org/licenses/MIT) 开源协议。

---

## 🙏 致谢

- [Anthropic](https://www.anthropic.com/) - Claude API
- [TianAPI](https://www.tianapi.com/) - 微博热搜数据
- [GitHub Actions](https://github.com/features/actions) - 自动化平台

---

## 📞 联系方式

- 💬 **Issues**: [提交问题](../../issues)
- 🌟 **Star**: 如果觉得有用，请给个 Star！
- 🔔 **Watch**: 关注项目更新

---

<div align="center">

**🤖 Powered by Claude API | AI 赋能产品创新**

Made with ❤️ by Claude Code

</div>
