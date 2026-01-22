# 🎯 立即操作清单 - GitHub Pages 部署

---

## 当前状态

✅ 代码已推送到 GitHub
✅ GitHub Pages 部署功能已配置
✅ workflow 文件已更新

---

## 接下来的 3 个步骤（10 分钟完成）

### 步骤 1️⃣: 配置 GitHub Secrets（5 分钟）

**如果你还没配置 Secrets，现在就配置：**

访问：https://github.com/xingyun7842/weibo-trending-analysis/settings/secrets/actions

**需要添加 4 个 Secrets：**

| Name | Value |
|------|-------|
| `ANTHROPIC_API_KEY` | `sk-WlhCHmgDcptriJCMM3oRYWSmVLPxQlcMVHF0iijBdNJSAJj5` |
| `ANTHROPIC_BASE_URL` | `https://yunwu.ai` |
| `ANTHROPIC_MODEL` | `claude-sonnet-4-5-20250929` |
| `TIANAPI_KEY` | `eda7b8c9c35234ce9a0dfd6939ae8c85` |

---

### 步骤 2️⃣: 手动运行 workflow（2 分钟）

访问：https://github.com/xingyun7842/weibo-trending-analysis/actions

1. 左侧点击 **"Weibo Trending Analysis"**
2. 右侧点击 **"Run workflow"** 下拉
3. 点击绿色 **"Run workflow"** 按钮
4. 等待运行完成（约 2 分钟）

**期望看到：**
- ✅ workflow 运行成功（绿色勾号）
- ✅ 自动创建 `gh-pages` 分支
- ✅ 部署报告到 GitHub Pages

---

### 步骤 3️⃣: 启用 GitHub Pages（3 分钟）

访问：https://github.com/xingyun7842/weibo-trending-analysis/settings/pages

**配置：**

```
Source: Deploy from a branch

Branch:
  ┌────────────────────┐
  │ gh-pages  /(root)  │  ← 选择这个
  └────────────────────┘

点击 "Save"
```

**等待 2-3 分钟后，页面顶部会显示：**
```
✅ Your site is live at
   https://xingyun7842.github.io/weibo-trending-analysis/
```

---

## 🌐 访问你的在线报告

**主页（自动跳转）：**
```
https://xingyun7842.github.io/weibo-trending-analysis/
```

**最新报告：**
```
https://xingyun7842.github.io/weibo-trending-analysis/latest.html
```

---

## ✅ 验证成功标志

- [ ] 4 个 Secrets 已配置
- [ ] workflow 运行成功（绿色勾号）
- [ ] GitHub Pages 已启用（Source: gh-pages）
- [ ] 网址可以访问
- [ ] 显示分析报告

全部打勾 = 部署成功！🎉

---

## 📱 分享给团队

部署成功后，直接分享这个链接：
```
https://xingyun7842.github.io/weibo-trending-analysis/
```

团队成员可以：
- ✅ 直接在浏览器查看
- ✅ 手机、平板访问
- ✅ 无需下载、无需登录

---

## 🔄 自动更新

配置完成后，系统将：
- ✅ 每天北京时间 10:00 自动运行
- ✅ 自动生成新报告
- ✅ 自动部署到网页
- ✅ 访问网址即可看到最新分析

---

## 💡 快速链接

| 功能 | 链接 |
|------|------|
| 📊 在线报告 | https://xingyun7842.github.io/weibo-trending-analysis/ |
| 🔐 配置 Secrets | https://github.com/xingyun7842/weibo-trending-analysis/settings/secrets/actions |
| 🚀 运行 Actions | https://github.com/xingyun7842/weibo-trending-analysis/actions |
| ⚙️ 配置 Pages | https://github.com/xingyun7842/weibo-trending-analysis/settings/pages |

---

**现在就开始第 1 步吧！** 🚀
