# ⚡ 你的专属配置清单（yunwu.ai）

---

## 🎯 第 1 步：复制你的 API 信息（已准备好）

✅ 以下信息已为你准备好，直接使用即可：

```yaml
API 端点:  https://yunwu.ai
API Key:   sk-WlhCHmgDcptriJCMM3oRYWSmVLPxQlcMVHF0iijBdNJSAJj5
模型名称:  claude-sonnet-4-5-20250929
```

---

## 🚀 第 2 步：配置 GitHub Secrets（5 分钟）

### 进入 Secrets 设置页面

```
1. 打开你的 GitHub 仓库
2. 点击 Settings 标签
3. 左侧菜单 → Secrets and variables → Actions
4. 准备添加 4 个 Secrets
```

---

### Secret 1/4: ANTHROPIC_API_KEY

```
点击 "New repository secret"

┌─────────────────────────────────────────────────────┐
│ Name:                                                │
│ ANTHROPIC_API_KEY                                    │
│                                                      │
│ Secret:                                              │
│ sk-WlhCHmgDcptriJCMM3oRYWSmVLPxQlcMVHF0iijBdNJSAJj5 │
└─────────────────────────────────────────────────────┘

点击 "Add secret" ✅
```

---

### Secret 2/4: ANTHROPIC_BASE_URL

```
点击 "New repository secret"

┌─────────────────────────────────────────────────────┐
│ Name:                                                │
│ ANTHROPIC_BASE_URL                                   │
│                                                      │
│ Secret:                                              │
│ https://yunwu.ai                                     │
└─────────────────────────────────────────────────────┘

点击 "Add secret" ✅
```

---

### Secret 3/4: ANTHROPIC_MODEL

```
点击 "New repository secret"

┌─────────────────────────────────────────────────────┐
│ Name:                                                │
│ ANTHROPIC_MODEL                                      │
│                                                      │
│ Secret:                                              │
│ claude-sonnet-4-5-20250929                           │
└─────────────────────────────────────────────────────┘

点击 "Add secret" ✅
```

---

### Secret 4/4: TIANAPI_KEY

```
点击 "New repository secret"

┌─────────────────────────────────────────────────────┐
│ Name:                                                │
│ TIANAPI_KEY                                          │
│                                                      │
│ Secret:                                              │
│ eda7b8c9c35234ce9a0dfd6939ae8c85                     │
└─────────────────────────────────────────────────────┘

点击 "Add secret" ✅
```

---

## ✅ 第 3 步：验证 Secrets

配置完成后，你的 Secrets 列表应该显示：

```
Secrets (4)
  ✅ ANTHROPIC_API_KEY
  ✅ ANTHROPIC_BASE_URL
  ✅ ANTHROPIC_MODEL
  ✅ TIANAPI_KEY
```

---

## 🎉 完成！现在可以部署了

所有配置已准备就绪，按照以下步骤继续：

### 立即执行：

```bash
# 1. 推送代码到 GitHub（如果还没推送）
cd "C:\Users\admin\Desktop\自动运行skill"
git add .
git commit -m "Update: Support third-party API (yunwu.ai)"
git push

# 2. 手动触发第一次运行
GitHub → Actions → Run workflow

# 3. 查看运行日志（应该显示）
🌐 使用第三方 API 端点: https://yunwu.ai
📋 使用模型: claude-sonnet-4-5-20250929

# 4. 下载报告
Artifacts → weibo-analysis-report-XXX
```

---

## 📋 完整部署流程

如果还没创建仓库，按此流程：

```
☐ 步骤 1: 创建 GitHub 仓库
   访问: https://github.com/new
   名称: weibo-trending-analysis

☐ 步骤 2: 配置 4 个 Secrets（见上方）
   ✓ ANTHROPIC_API_KEY
   ✓ ANTHROPIC_BASE_URL
   ✓ ANTHROPIC_MODEL
   ✓ TIANAPI_KEY

☐ 步骤 3: 推送代码
   cd "C:\Users\admin\Desktop\自动运行skill"
   git init
   git add .
   git commit -m "Initial commit with third-party API support"
   git remote add origin https://github.com/你的用户名/weibo-trending-analysis.git
   git push -u origin main

☐ 步骤 4: 手动触发运行
   Actions → Run workflow

☐ 步骤 5: 下载报告
   Artifacts → 下载 HTML
```

---

## 💡 重要提示

### ⚠️ 注意复制格式

**API Key 复制时确保**:
- ✅ 完整复制（不要漏字符）
- ✅ 无多余空格
- ✅ 无换行符

**Base URL 格式**:
- ✅ 正确: `https://yunwu.ai`
- ❌ 错误: `https://yunwu.ai/`（末尾有斜杠）
- ❌ 错误: `yunwu.ai`（缺少 https://）

---

## 🎊 预期效果

运行成功后你会看到：

```
📡 正在获取微博热搜数据...
✅ 成功获取 50 条热搜话题

🔍 开始分析前 15 个热点...

🌐 使用第三方 API 端点: https://yunwu.ai  ← 这里！
🤖 正在调用 Claude API 进行深度分析...
📋 使用模型: claude-sonnet-4-5-20250929    ← 这里！
⏳ 这可能需要 1-2 分钟，请耐心等待...

✅ 分析完成！
📊 分析统计:
   - 优秀创意 (≥80分): 3 个
   - 良好创意 (60-79分): 8 个
   - 产品创意总数: 28 个

✅ HTML 报告已生成
```

---

## 📞 遇到问题？

### 检查清单

1. **所有 4 个 Secrets 都配置了吗？**
   - Settings → Secrets → 应该看到 4 个

2. **API Key 复制正确吗？**
   - 以 `sk-` 开头
   - 完整无遗漏

3. **Base URL 格式正确吗？**
   - `https://yunwu.ai`（无末尾斜杠）

4. **模型名称正确吗？**
   - `claude-sonnet-4-5-20250929`

5. **代码已推送到 GitHub 了吗？**
   - 仓库中应该有最新的代码

### 查看错误日志

```
GitHub → Actions → 选择运行 → 点击 job → 查看详细日志
```

错误通常会清楚显示是哪个配置有问题。

---

## 🚀 开始部署吧！

所有信息已准备完毕，现在就可以开始部署了！

**祝你部署顺利！** 🎉

---

**配置时间**: ~5 分钟
**第三方 API**: yunwu.ai
**模型**: claude-sonnet-4-5-20250929
**生成时间**: 2026-01-20
