# GitHub Secrets 配置指南

## 🔐 必需的 Secrets

在 GitHub 仓库中配置以下 Secrets，这些是运行自动化分析所必需的：

### 1. ANTHROPIC_API_KEY

**用途**: 调用 Claude API 进行热点分析和产品创意生成

**如何获取**:
1. 访问 [Anthropic Console](https://console.anthropic.com/)
2. 登录或注册账号
3. 进入 "API Keys" 页面
4. 点击 "Create Key" 创建新的 API 密钥
5. 复制生成的密钥（格式: `sk-ant-api03-...`）

**费用说明**:
- 使用 Claude 3.5 Sonnet 模型
- 每次分析约消耗 10,000-20,000 tokens
- 成本约 $0.10-0.30 USD/次
- 建议设置使用限额

**配置位置**:
```
GitHub Repository → Settings → Secrets and variables → Actions → New repository secret
Name: ANTHROPIC_API_KEY
Secret: sk-ant-api03-xxxxx...
```

---

### 2. TIANAPI_KEY

**用途**: 获取微博热搜实时数据

**如何获取**:
1. 访问 [TianAPI 官网](https://www.tianapi.com/)
2. 注册账号并登录
3. 进入 [API 市场](https://www.tianapi.com/apiview/223) 找到"微博热搜榜"
4. 点击"申请接口"
5. 在个人中心 → API 管理 中查看你的 API Key

**免费额度**:
- 免费用户: 100 次/天
- VIP 用户: 更高额度
- 如果使用默认密钥 `eda7b8c9c35234ce9a0dfd6939ae8c85`，可能被多人共享

**配置位置**:
```
GitHub Repository → Settings → Secrets and variables → Actions → New repository secret
Name: TIANAPI_KEY
Secret: eda7b8c9c35234ce9a0dfd6939ae8c85
```

**重要提示**:
- 建议申请自己的 API Key 以避免额度冲突
- 默认密钥仅用于测试，生产环境请使用自己的密钥

---

## ⚙️ 可选配置

### Environment Variables（可在 workflow 中直接修改）

这些参数可以在 `.github/workflows/weibo-analysis.yml` 中修改：

```yaml
env:
  MAX_TOPICS: '15'              # 分析的热点数量（建议 10-20）
  MIN_SCORE_EXCELLENT: '80'     # 优秀创意的最低分数
  MIN_SCORE_GOOD: '60'          # 良好创意的最低分数
```

---

## 📋 配置步骤

### 步骤 1: 进入仓库设置

1. 打开你的 GitHub 仓库
2. 点击 `Settings` 标签
3. 在左侧菜单找到 `Secrets and variables` → `Actions`

### 步骤 2: 添加 ANTHROPIC_API_KEY

1. 点击 `New repository secret` 按钮
2. 在 `Name` 字段输入: `ANTHROPIC_API_KEY`
3. 在 `Secret` 字段粘贴你的 Claude API 密钥
4. 点击 `Add secret` 保存

### 步骤 3: 添加 TIANAPI_KEY

1. 再次点击 `New repository secret`
2. 在 `Name` 字段输入: `TIANAPI_KEY`
3. 在 `Secret` 字段粘贴你的 TianAPI 密钥
4. 点击 `Add secret` 保存

### 步骤 4: 验证配置

检查你的 Secrets 列表应该包含：
- ✅ `ANTHROPIC_API_KEY`
- ✅ `TIANAPI_KEY`

---

## 🔍 安全最佳实践

### 1. 密钥保护
- ❌ 不要将 API 密钥硬编码在代码中
- ❌ 不要将密钥提交到 Git 仓库
- ✅ 始终使用 GitHub Secrets 存储敏感信息
- ✅ 定期轮换 API 密钥

### 2. 权限控制
- 使用只读 API 密钥（如果平台支持）
- 为 Claude API 设置使用限额
- 监控 API 调用次数和费用

### 3. 访问限制
- 仅授权必要的 GitHub Actions 权限
- 使用环境保护规则（Environment protection rules）
- 审计 Actions 运行日志

---

## 🐛 故障排查

### 问题 1: "ANTHROPIC_API_KEY not set"

**原因**: GitHub Secrets 未正确配置

**解决方案**:
1. 检查 Secret 名称是否完全匹配（大小写敏感）
2. 确认 Secret 已保存（刷新页面查看）
3. 重新运行 workflow

### 问题 2: "Invalid API key"

**原因**: API 密钥无效或已过期

**解决方案**:
1. 登录 Anthropic Console 验证密钥状态
2. 生成新的 API 密钥
3. 更新 GitHub Secret

### 问题 3: "TianAPI quota exceeded"

**原因**: API 调用次数超过限额

**解决方案**:
1. 检查 TianAPI 账户配额
2. 申请更高配额或购买 VIP
3. 调整 workflow 运行频率（减少 cron 触发）

### 问题 4: API 密钥泄露

**紧急处理**:
1. 立即撤销泄露的密钥
2. 生成新密钥并更新 GitHub Secret
3. 检查是否有异常 API 调用
4. 审查 Git 历史，确保密钥未提交

---

## 💰 成本估算

### Claude API 费用

基于 Claude 3.5 Sonnet 定价:
- Input: $3.00 / 1M tokens
- Output: $15.00 / 1M tokens

**单次分析成本**:
- 输入 tokens: ~5,000-8,000（热点数据 + prompt）
- 输出 tokens: ~8,000-12,000（分析结果）
- 估算成本: $0.10 - 0.30 USD

**每日自动运行**:
- 1 次/天 × 30 天 = $3 - 9 USD/月

### TianAPI 费用

- 免费版: 100 次/天（完全免费）
- VIP 版: 更高额度（需付费）

**建议**:
- 对于测试：使用免费额度
- 对于生产：考虑购买 Claude API 信用额度

---

## 📞 获取帮助

- **Anthropic API 文档**: https://docs.anthropic.com/
- **TianAPI 文档**: https://www.tianapi.com/console/
- **GitHub Actions 文档**: https://docs.github.com/actions

---

**最后更新**: 2026-01-20
**维护者**: GitHub Actions Automation
