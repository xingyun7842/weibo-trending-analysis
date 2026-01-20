# ⚡ 快速部署指南（10 分钟完成）

---

## 📋 准备清单

在开始之前，请确保你已准备好：

- ✅ GitHub 账号
- ✅ Anthropic API Key（[点击获取](https://console.anthropic.com/)）
- ✅ 安装了 Git

---

## 🚀 部署步骤（只需 4 步！）

### 步骤 1️⃣: 创建 GitHub 仓库（2 分钟）

```bash
1. 访问: https://github.com/new

2. 填写信息:
   Repository name: weibo-trending-analysis
   Visibility: ⚪ Private (推荐)

3. ❌ 不要勾选 "Initialize this repository with a README"

4. 点击 "Create repository"

5. 复制仓库 URL:
   https://github.com/你的用户名/weibo-trending-analysis.git
```

---

### 步骤 2️⃣: 配置 GitHub Secrets（3 分钟）

```bash
1. 在新创建的仓库页面:
   Settings → Secrets and variables → Actions

2. 点击 "New repository secret"

3. 添加第一个 Secret:
   Name:   ANTHROPIC_API_KEY
   Secret: sk-ant-api03-你的密钥
   点击 "Add secret"

4. 再次点击 "New repository secret"

5. 添加第二个 Secret:
   Name:   TIANAPI_KEY
   Secret: eda7b8c9c35234ce9a0dfd6939ae8c85
   点击 "Add secret"

6. 确认两个 Secrets 都已添加 ✅
```

> 💡 **Anthropic API Key 获取**:
> 1. 访问 https://console.anthropic.com/
> 2. 登录后进入 "API Keys"
> 3. 点击 "Create Key"
> 4. 复制生成的密钥（格式: sk-ant-api03-...）

---

### 步骤 3️⃣: 推送代码到 GitHub（3 分钟）

打开命令提示符/终端，执行以下命令：

```bash
# 1. 进入项目目录
cd "C:\Users\admin\Desktop\自动运行skill"

# 2. 初始化 Git（如果还没有）
git init

# 3. 添加所有文件
git add .

# 4. 创建首次提交
git commit -m "Initial commit: Weibo trending analysis with GitHub Actions"

# 5. 关联远程仓库（替换为你的仓库 URL）
git remote add origin https://github.com/你的用户名/weibo-trending-analysis.git

# 6. 推送到 GitHub
git branch -M main
git push -u origin main
```

**如果遇到认证问题**，使用 Personal Access Token：

```bash
# 生成 Token: https://github.com/settings/tokens
# 权限选择: repo (完整仓库访问)

# 推送时使用 Token 作为密码
git push https://你的用户名:你的Token@github.com/你的用户名/weibo-trending-analysis.git
```

---

### 步骤 4️⃣: 手动触发首次运行（2 分钟）

```bash
1. 刷新 GitHub 仓库页面

2. 点击 "Actions" 标签

3. 左侧选择 "Weibo Trending Analysis"

4. 右侧点击 "Run workflow" 下拉按钮

5. (可选) 修改 max_topics（默认 15）

6. 点击绿色 "Run workflow" 按钮

7. 等待 1-2 分钟，刷新页面

8. 点击最新的 workflow run 查看进度
```

**查看运行日志**：
- 展开 "analyze-trends" job
- 查看各步骤执行情况
- ✅ 绿色勾号 = 成功
- ❌ 红色叉号 = 失败（查看错误信息）

---

## 📥 下载分析报告

运行成功后：

```bash
1. 在 workflow run 页面向下滚动

2. 找到 "Artifacts" 部分

3. 点击下载 "weibo-analysis-report-XXX"

4. 解压 ZIP 文件

5. 在浏览器中打开 HTML 文件 🎉
```

---

## 🎯 验证成功标志

如果看到以下内容，说明部署成功：

```
✅ Actions 页面显示绿色勾号
✅ Summary 显示分析统计
✅ Artifacts 中有 HTML 报告
✅ HTML 报告包含热点分析和产品创意
```

---

## ⏰ 设置定时运行

部署成功后，workflow 将自动按以下时间运行：

```yaml
每天北京时间 10:00 (UTC 2:00)
```

**修改运行时间**：

编辑 `.github/workflows/weibo-analysis.yml` 文件：

```yaml
schedule:
  # 每天早上 8:00 (UTC 0:00)
  - cron: '0 0 * * *'

  # 每 12 小时一次
  # - cron: '0 */12 * * *'

  # 每周一早上 9:00 (UTC 1:00)
  # - cron: '0 1 * * 1'
```

修改后推送：
```bash
git add .github/workflows/weibo-analysis.yml
git commit -m "Update schedule"
git push
```

---

## 🐛 常见问题快速解决

### ❌ 问题：推送失败 "Permission denied"

**解决方案**：
```bash
# 使用 HTTPS + Personal Access Token
git remote set-url origin https://你的Token@github.com/你的用户名/仓库名.git
git push
```

---

### ❌ 问题：Actions 显示 "ANTHROPIC_API_KEY not set"

**解决方案**：
1. 检查 Secret 名称拼写（区分大小写）
2. 重新创建 Secret
3. 重新运行 workflow

---

### ❌ 问题：Claude API 调用失败

**检查清单**：
- API Key 格式正确（sk-ant-api03-...）
- Anthropic 账户有余额
- 在 Anthropic Console 查看 API 使用状态

---

## 💰 成本说明

- **Claude API**: ~$0.20 USD/次
- **每月成本**: ~$6 USD（每天运行 1 次）
- **TianAPI**: 免费（100次/天）

**节省成本**：
- 减少运行频率（如每周 1 次）
- 减少分析热点数量（如改为 10 个）
- 设置 API 使用限额

---

## 📚 完整文档

| 文档 | 说明 |
|------|------|
| `README.md` | 项目介绍和功能特性 |
| `DEPLOYMENT_GUIDE.md` | 详细部署教程 |
| `SECRETS_SETUP.md` | API 密钥配置指南 |
| `MIGRATION_SUMMARY.md` | 技术可行性分析报告 |
| `QUICK_START.md` | 本文档（快速开始） |

---

## 🎉 完成！

恭喜！你已经成功部署了自动化微博热搜分析系统！

**接下来**：
- 每天自动生成分析报告
- 在 Actions → Artifacts 中下载报告
- 发现产品创意机会 💡

**需要帮助**？
- 查看完整文档：`DEPLOYMENT_GUIDE.md`
- 提交 Issue 到 GitHub 仓库

---

**部署时间**: ~10 分钟
**维护成本**: ~$6/月
**价值**: 无价（自动化产品创意挖掘）🚀
