# 🎯 最终部署指南 - 3 个步骤完成

---

## 当前状态

✅ 代码已推送到 GitHub
✅ workflow 已配置完成
✅ GitHub Pages 部署功能已集成

---

## 📋 完整部署流程（3 步）

### 步骤 1️⃣: 配置 GitHub Secrets（5 分钟）

访问：https://github.com/xingyun7842/weibo-trending-analysis/settings/secrets/actions

点击 **"New repository secret"**，逐个添加以下 4 个 Secrets：

```
Secret 1/4:
  Name:   ANTHROPIC_API_KEY
  Secret: sk-WlhCHmgDcptriJCMM3oRYWSmVLPxQlcMVHF0iijBdNJSAJj5

Secret 2/4:
  Name:   ANTHROPIC_BASE_URL
  Secret: https://yunwu.ai

Secret 3/4:
  Name:   ANTHROPIC_MODEL
  Secret: claude-sonnet-4-5-20250929

Secret 4/4:
  Name:   TIANAPI_KEY
  Secret: eda7b8c9c35234ce9a0dfd6939ae8c85
```

**验证**：配置完成后应该看到 4 个 Secrets

---

### 步骤 2️⃣: 启用 GitHub Pages（1 分钟）⭐ 重要

访问：https://github.com/xingyun7842/weibo-trending-analysis/settings/pages

在 **"Build and deployment"** 部分：

```
Source (来源):
  选择: GitHub Actions  ← 选择这个！
```

**就这样！** 不需要选择分支，选择 "GitHub Actions" 即可。

**为什么需要这一步？**
- 这是启用 GitHub Pages 的开关
- **只需设置一次**，之后 workflow 会自动部署
- 官方 `actions/deploy-pages@v4` 要求先启用这个功能

---

### 步骤 3️⃣: 运行 workflow（2 分钟）

访问：https://github.com/xingyun7842/weibo-trending-analysis/actions

1. 左侧选择 **"Weibo Trending Analysis"**
2. 右侧点击 **"Run workflow"** 下拉按钮
3. 点击绿色 **"Run workflow"** 按钮
4. 等待运行完成（约 2 分钟）

**期望看到的步骤**：
```
✅ Checkout repository
✅ Set up Python
✅ Install dependencies
✅ Run Weibo Analysis with Claude Agent SDK
✅ Upload HTML Report as Artifact
✅ Commit and Push Report
✅ Setup GitHub Pages
✅ Upload Pages Artifact
✅ Deploy to GitHub Pages  ← 自动部署！
✅ Summary
```

---

## 🌐 访问在线报告

workflow 运行成功后，访问：

```
https://xingyun7842.github.io/weibo-trending-analysis/
```

**首次访问可能需要等待 2-3 分钟让 GitHub Pages 完成发布。**

---

## 🔄 后续自动运行

配置完成后，系统将：
- ✅ 每天北京时间 10:00 自动运行
- ✅ 自动生成分析报告
- ✅ 自动部署到 GitHub Pages
- ✅ 访问网址即可看到最新分析

**无需再做任何手动操作！**

---

## ✅ 完整检查清单

```
☐ 步骤 1: 配置 4 个 GitHub Secrets
☐ 步骤 2: 启用 GitHub Pages (Source: GitHub Actions)
☐ 步骤 3: 手动运行一次 workflow
☐ 验证: workflow 运行成功（绿色勾号）
☐ 验证: 可以访问在线报告
```

全部打勾 = 部署完成！🎉

---

## 📊 工作流程图

```
第一次设置（3 步）:
  1. 配置 Secrets
  2. 启用 GitHub Pages (Source: GitHub Actions) ← 只需一次
  3. 运行 workflow
     ↓
  GitHub Pages 发布完成
     ↓
  访问在线报告 ✅

后续自动运行:
  每天 10:00 自动触发
     ↓
  workflow 自动运行
     ↓
  自动部署到 GitHub Pages
     ↓
  在线报告自动更新 ✅
```

---

## 💡 关键说明

### 为什么需要手动启用 GitHub Pages？

使用官方 `actions/deploy-pages@v4` 的优势：
- ✅ 更稳定、更安全
- ✅ 官方支持
- ✅ 不需要创建额外的 gh-pages 分支
- ✅ 直接从 workflow artifacts 部署

**代价**：需要在 Settings 里一次性设置 Source 为 "GitHub Actions"

### 只需设置一次

启用 GitHub Pages 后：
- ✅ workflow 每次运行都会自动部署
- ✅ 不需要再去 Settings 配置
- ✅ 完全自动化

---

## 🔗 快速链接

| 步骤 | 链接 |
|------|------|
| 步骤 1: 配置 Secrets | https://github.com/xingyun7842/weibo-trending-analysis/settings/secrets/actions |
| 步骤 2: 启用 Pages | https://github.com/xingyun7842/weibo-trending-analysis/settings/pages |
| 步骤 3: 运行 workflow | https://github.com/xingyun7842/weibo-trending-analysis/actions |
| 在线报告 | https://xingyun7842.github.io/weibo-trending-analysis/ |

---

## 🐛 故障排查

### 问题：workflow 运行失败，提示 Pages 权限错误

**解决**：
1. 确认步骤 2 已完成（启用 GitHub Pages）
2. 确认 Source 选择的是 "GitHub Actions"
3. 重新运行 workflow

### 问题：404 Not Found

**原因**：首次部署需要时间

**解决**：
- 等待 2-3 分钟后刷新
- 确认 workflow 运行成功
- 检查 Settings → Pages 是否显示网址

---

**现在就开始第 1 步吧！** 🚀

总计时间：~8 分钟
步骤数：3 步
难度：⭐⭐ (简单)
