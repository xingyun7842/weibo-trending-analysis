# 设置 Claude Code 为完全免授权模式
# 运行此脚本后，在当前 PowerShell 会话中启动 claude 将自动跳过权限确认

# 设置环境变量
$env:CLAUDE_SKIP_PERMISSIONS = "true"

Write-Host "已启用 bypass permissions 模式" -ForegroundColor Green
Write-Host "现在可以运行: claude" -ForegroundColor Yellow
Write-Host ""
Write-Host "注意: 此设置仅在当前 PowerShell 会话有效" -ForegroundColor Cyan
Write-Host "如需永久设置，请将环境变量添加到系统环境变量中" -ForegroundColor Cyan
