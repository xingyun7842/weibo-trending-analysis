# 🎯 xingyun7842 的 GitHub Secrets 配置速查卡

---

## ✅ 第 1 步：打开配置页面

**直接点击这个链接**：
```
https://github.com/xingyun7842/weibo-trending-analysis/settings/secrets/actions
```

然后点击 **"New repository secret"** 按钮

---

## 📋 第 2 步：复制粘贴以下 4 个 Secrets

### Secret 1/4

```
Name:
ANTHROPIC_API_KEY

Secret:
sk-WlhCHmgDcptriJCMM3oRYWSmVLPxQlcMVHF0iijBdNJSAJj5
```

点击 **"Add secret"** ✅

---

### Secret 2/4

```
Name:
ANTHROPIC_BASE_URL

Secret:
https://yunwu.ai
```

⚠️ **重要**：确保无末尾斜杠！

点击 **"Add secret"** ✅

---

### Secret 3/4

```
Name:
ANTHROPIC_MODEL

Secret:
claude-sonnet-4-5-20250929
```

点击 **"Add secret"** ✅

---

### Secret 4/4

```
Name:
TIANAPI_KEY

Secret:
eda7b8c9c35234ce9a0dfd6939ae8c85
```

点击 **"Add secret"** ✅

---

## ✅ 第 3 步：验证配置

配置完成后，Secrets 列表应显示：

```
Repository secrets (4)
  ✅ ANTHROPIC_API_KEY
  ✅ ANTHROPIC_BASE_URL
  ✅ ANTHROPIC_MODEL
  ✅ TIANAPI_KEY
```

---

## 🚀 第 4 步：手动触发运行

**直接点击这个链接**：
```
https://github.com/xingyun7842/weibo-trending-analysis/actions
```

1. 左侧选择 **"Weibo Trending Analysis"**
2. 右侧点击 **"Run workflow"** 下拉
3. 点击绿色 **"Run workflow"** 按钮
4. 等待 1-2 分钟，刷新查看结果

---

## 📥 第 5 步：下载报告

运行成功后：
1. 滚动到页面底部 **"Artifacts"**
2. 点击下载 **"weibo-analysis-report-XXX"**
3. 解压 ZIP 并打开 HTML 文件

---

## 🔗 快速链接合集

| 功能 | 链接 |
|------|------|
| 仓库主页 | https://github.com/xingyun7842/weibo-trending-analysis |
| 配置 Secrets | https://github.com/xingyun7842/weibo-trending-analysis/settings/secrets/actions |
| 运行 Actions | https://github.com/xingyun7842/weibo-trending-analysis/actions |
| 查看代码 | https://github.com/xingyun7842/weibo-trending-analysis/tree/main |

---

## ⏰ 自动运行时间

配置完成后，系统将：
- ✅ 每天北京时间 **10:00** 自动运行
- ✅ 自动生成分析报告
- ✅ 报告保存 90 天

---

## 💡 快速提示

**复制技巧**：
- 使用鼠标三击选中整行
- Ctrl+C 复制
- 在 GitHub 页面 Ctrl+V 粘贴

**注意事项**：
- Secret 名称必须完全匹配（区分大小写）
- Secret 值不要有多余空格
- ANTHROPIC_BASE_URL 末尾不要有斜杠

---

**配置时间**：约 5 分钟
**用户**：xingyun7842
**仓库**：weibo-trending-analysis
**生成时间**：2026-01-20
