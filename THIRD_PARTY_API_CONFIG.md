# 🔐 第三方 API 配置指南（yunwu.ai）

---

## ✅ 你的第三方 API 信息

根据你提供的信息：

| 配置项 | 值 |
|--------|-----|
| **API 端点** | `https://yunwu.ai` |
| **API Key** | `sk-WlhCHmgDcptriJCMM3oRYWSmVLPxQlcMVHF0iijBdNJSAJj5` |
| **模型名称** | `claude-sonnet-4-5-20250929` |

---

## 🔑 需要配置的 GitHub Secrets（3 个）

### 必需的 Secrets

在 GitHub 仓库中配置以下 **3 个** Secrets：

#### 1. ANTHROPIC_API_KEY ⭐

```
Name:   ANTHROPIC_API_KEY
Secret: sk-WlhCHmgDcptriJCMM3oRYWSmVLPxQlcMVHF0iijBdNJSAJj5
```

**说明**: 你的第三方 Claude API 密钥

---

#### 2. ANTHROPIC_BASE_URL ⭐ 新增

```
Name:   ANTHROPIC_BASE_URL
Secret: https://yunwu.ai
```

**说明**: 第三方 API 的请求地址（替代官方 api.anthropic.com）

---

#### 3. ANTHROPIC_MODEL ⭐ 新增

```
Name:   ANTHROPIC_MODEL
Secret: claude-sonnet-4-5-20250929
```

**说明**: 自定义模型名称

---

#### 4. TIANAPI_KEY

```
Name:   TIANAPI_KEY
Secret: eda7b8c9c35234ce9a0dfd6939ae8c85
```

**说明**: 微博热搜 API 密钥（使用默认密钥）

---

## 📋 配置步骤（5 分钟）

### 步骤 1: 进入 Secrets 设置

```
GitHub 仓库页面
  → Settings 标签
  → Secrets and variables（左侧菜单）
  → Actions
```

### 步骤 2: 添加第 1 个 Secret

```
点击 "New repository secret"

Name:   ANTHROPIC_API_KEY
Secret: sk-WlhCHmgDcptriJCMM3oRYWSmVLPxQlcMVHF0iijBdNJSAJj5

点击 "Add secret"
```

### 步骤 3: 添加第 2 个 Secret

```
点击 "New repository secret"

Name:   ANTHROPIC_BASE_URL
Secret: https://yunwu.ai

点击 "Add secret"
```

### 步骤 4: 添加第 3 个 Secret

```
点击 "New repository secret"

Name:   ANTHROPIC_MODEL
Secret: claude-sonnet-4-5-20250929

点击 "Add secret"
```

### 步骤 5: 添加第 4 个 Secret

```
点击 "New repository secret"

Name:   TIANAPI_KEY
Secret: eda7b8c9c35234ce9a0dfd6939ae8c85

点击 "Add secret"
```

---

## ✅ 验证配置

配置完成后，你的 Secrets 列表应该显示：

```
✅ ANTHROPIC_API_KEY
✅ ANTHROPIC_BASE_URL
✅ ANTHROPIC_MODEL
✅ TIANAPI_KEY
```

**总计: 4 个 Secrets**

---

## 🎯 配置对比

### 官方 Anthropic API（标准配置）

```yaml
Secrets:
  - ANTHROPIC_API_KEY: sk-ant-api03-xxxxx...
  - TIANAPI_KEY: eda7b8c9c35234ce9a0dfd6939ae8c85

总计: 2 个
```

### 第三方 API（你的配置）⭐

```yaml
Secrets:
  - ANTHROPIC_API_KEY: sk-WlhCHmgDcptriJCMM3oRYWSmVLPxQlcMVHF0iijBdNJSAJj5
  - ANTHROPIC_BASE_URL: https://yunwu.ai
  - ANTHROPIC_MODEL: claude-sonnet-4-5-20250929
  - TIANAPI_KEY: eda7b8c9c35234ce9a0dfd6939ae8c85

总计: 4 个
```

---

## 🔧 技术实现

脚本已更新支持第三方 API：

```python
# scripts/weibo_analysis_agent.py

# 从环境变量读取配置
ANTHROPIC_BASE_URL = os.getenv("ANTHROPIC_BASE_URL", None)
ANTHROPIC_MODEL = os.getenv("ANTHROPIC_MODEL", "claude-3-5-sonnet-20241022")

# 创建客户端时使用自定义端点
client_kwargs = {"api_key": anthropic_api_key}

if ANTHROPIC_BASE_URL:
    client_kwargs["base_url"] = ANTHROPIC_BASE_URL

client = Anthropic(**client_kwargs)

# 调用 API 时使用自定义模型
response = client.messages.create(
    model=ANTHROPIC_MODEL,  # 使用你的模型名称
    max_tokens=16000,
    ...
)
```

---

## 💰 成本说明

### 第三方 API

- **费用**: 根据你的第三方服务商定价
- **计费方式**: 请咨询 yunwu.ai 的具体定价
- **优势**: 通常比官方 API 更便宜，国内访问更快

### TianAPI

- **费用**: 免费（100 次/天）
- **升级**: 如需更高额度可购买 VIP

---

## ⚠️ 注意事项

### 1. API 密钥安全

❌ **不要**将你的 API Key 分享给他人
❌ **不要**在代码中硬编码 API Key
✅ **必须**使用 GitHub Secrets 存储
✅ **建议**定期更换密钥

### 2. API 端点格式

**正确格式**:
```
https://yunwu.ai
```

**错误格式**:
```
https://yunwu.ai/     ❌ (末尾不要斜杠)
https://yunwu.ai/v1   ❌ (不要包含路径)
yunwu.ai              ❌ (必须包含 https://)
```

### 3. 模型名称

确保模型名称与第三方 API 支持的完全一致：
```
claude-sonnet-4-5-20250929  ✅
claude-3-5-sonnet           ❌ (可能不匹配)
```

---

## 🐛 故障排查

### 问题 1: API 调用失败

**错误信息**: "Connection error" 或 "Invalid endpoint"

**检查清单**:
- [ ] `ANTHROPIC_BASE_URL` 格式正确（无末尾斜杠）
- [ ] URL 以 `https://` 开头
- [ ] 网络可以访问 yunwu.ai
- [ ] Secret 名称拼写正确（区分大小写）

**解决方案**:
```bash
# 在 Actions 运行日志中查看详细错误
GitHub → Actions → 选择运行 → 查看日志
```

---

### 问题 2: 模型不支持

**错误信息**: "Model not found" 或 "Invalid model"

**检查清单**:
- [ ] `ANTHROPIC_MODEL` 拼写正确
- [ ] 模型名称与第三方 API 文档一致
- [ ] Secret 值中没有多余空格

**解决方案**:
1. 访问 yunwu.ai 文档确认支持的模型列表
2. 更新 `ANTHROPIC_MODEL` Secret

---

### 问题 3: API Key 无效

**错误信息**: "Invalid API key" 或 "Authentication failed"

**检查清单**:
- [ ] API Key 完整复制（无遗漏字符）
- [ ] API Key 未过期
- [ ] 账户余额充足（如有要求）

**解决方案**:
1. 重新复制 API Key（避免多余空格）
2. 更新 `ANTHROPIC_API_KEY` Secret
3. 联系 yunwu.ai 验证账户状态

---

## 📊 运行日志示例

成功运行时的日志输出：

```
📡 正在获取微博热搜数据...
✅ 成功获取 50 条热搜话题

🔍 开始分析前 15 个热点...

🌐 使用第三方 API 端点: https://yunwu.ai
🤖 正在调用 Claude API 进行深度分析...
📋 使用模型: claude-sonnet-4-5-20250929
⏳ 这可能需要 1-2 分钟，请耐心等待...

✅ 分析完成！

📊 分析统计:
   - 总计分析: 15 个热点
   - 优秀创意 (≥80分): 3 个
   - 良好创意 (60-79分): 8 个
   - 产品创意总数: 28 个

📝 正在生成 HTML 报告...
✅ HTML 报告已生成: reports/weibo_trending_analysis_20260120_143025.html

✨ 分析完成！
```

---

## 🎉 配置完成检查清单

部署前请确认：

- [ ] 4 个 Secrets 全部配置完成
- [ ] API Key 格式正确（sk- 开头）
- [ ] Base URL 格式正确（https:// 开头，无末尾斜杠）
- [ ] 模型名称与服务商文档一致
- [ ] 代码已推送到 GitHub
- [ ] 准备手动触发第一次运行

---

## 📞 需要帮助？

**第三方 API 问题**:
- 联系 yunwu.ai 技术支持
- 查看服务商文档: https://yunwu.ai/docs

**GitHub Actions 问题**:
- 查看 `DEPLOYMENT_GUIDE.md`
- 检查 Actions 运行日志

---

**配置版本**: v1.1 (第三方 API 支持)
**最后更新**: 2026-01-20
**支持的第三方服务**: yunwu.ai 及其他兼容 Anthropic SDK 的服务
