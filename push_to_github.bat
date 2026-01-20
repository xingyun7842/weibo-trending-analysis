@echo off
chcp 65001 >nul
echo ╔════════════════════════════════════════════════════════════════╗
echo ║                                                                 ║
echo ║           GitHub 一键推送脚本（第三方 API 版本）                ║
echo ║                                                                 ║
echo ╚════════════════════════════════════════════════════════════════╝
echo.
echo 📋 使用说明：
echo    1. 请先在 GitHub 创建好仓库
echo    2. 准备好你的 GitHub 用户名
echo    3. 准备好你的仓库名（如: weibo-trending-analysis）
echo.
pause
echo.

REM 获取用户输入
set /p GITHUB_USERNAME="请输入你的 GitHub 用户名: "
set /p REPO_NAME="请输入你的仓库名称（默认: weibo-trending-analysis）: "

REM 使用默认仓库名
if "%REPO_NAME%"=="" set REPO_NAME=weibo-trending-analysis

echo.
echo ✅ 配置信息:
echo    GitHub 用户名: %GITHUB_USERNAME%
echo    仓库名称: %REPO_NAME%
echo    仓库 URL: https://github.com/%GITHUB_USERNAME%/%REPO_NAME%.git
echo.
echo ⚠️  请确认以上信息正确
pause
echo.

REM 检查是否已经初始化
if exist .git (
    echo 📁 检测到已存在 .git 目录
    echo.
    set /p REINIT="是否重新初始化？(y/n，默认 n): "
    if /i "%REINIT%"=="y" (
        echo 🗑️  删除现有 .git 目录...
        rmdir /s /q .git
        echo ✅ 已删除
    )
)

REM 初始化 Git
if not exist .git (
    echo.
    echo 📦 步骤 1/4: 初始化 Git 仓库...
    git init
    if errorlevel 1 (
        echo ❌ Git 初始化失败，请检查是否安装了 Git
        pause
        exit /b 1
    )
    echo ✅ Git 初始化成功
)

REM 添加文件
echo.
echo 📦 步骤 2/4: 添加所有文件...
git add .
if errorlevel 1 (
    echo ❌ 添加文件失败
    pause
    exit /b 1
)
echo ✅ 文件已添加

REM 创建提交
echo.
echo 📦 步骤 3/4: 创建提交...
git commit -m "Add third-party API support (yunwu.ai) for weibo trending analysis"
if errorlevel 1 (
    echo ⚠️  提交失败（可能没有新的更改）
    echo 继续执行...
)
echo ✅ 提交完成

REM 设置远程仓库
echo.
echo 📦 步骤 4/4: 配置远程仓库...

REM 检查是否已存在 origin
git remote | findstr "origin" >nul
if %errorlevel%==0 (
    echo 🔄 远程仓库 origin 已存在，正在更新...
    git remote set-url origin https://github.com/%GITHUB_USERNAME%/%REPO_NAME%.git
) else (
    echo 🔗 添加远程仓库...
    git remote add origin https://github.com/%GITHUB_USERNAME%/%REPO_NAME%.git
)

if errorlevel 1 (
    echo ❌ 配置远程仓库失败
    pause
    exit /b 1
)
echo ✅ 远程仓库配置成功

REM 切换到 main 分支
echo.
echo 🌿 切换到 main 分支...
git branch -M main
echo ✅ 已切换到 main 分支

REM 推送到 GitHub
echo.
echo ════════════════════════════════════════════════════════════════
echo 🚀 准备推送到 GitHub
echo ════════════════════════════════════════════════════════════════
echo.
echo 📌 提示：
echo    - 如果是第一次推送，需要输入 GitHub 凭证
echo    - 密码处请使用 Personal Access Token（不是账户密码）
echo    - Token 获取: https://github.com/settings/tokens
echo.
pause
echo.
echo 📤 正在推送...
git push -u origin main

if errorlevel 1 (
    echo.
    echo ❌ 推送失败！
    echo.
    echo 💡 可能的原因:
    echo    1. GitHub 认证失败
    echo    2. 仓库不存在或 URL 错误
    echo    3. 网络连接问题
    echo.
    echo 💡 解决方案:
    echo    方法 1: 使用 Personal Access Token
    echo      访问: https://github.com/settings/tokens
    echo      创建 Token（勾选 repo 权限）
    echo      推送时使用 Token 作为密码
    echo.
    echo    方法 2: 使用 HTTPS + Token 直接推送
    echo      git push https://你的Token@github.com/%GITHUB_USERNAME%/%REPO_NAME%.git
    echo.
    echo    方法 3: 配置 SSH（推荐长期使用）
    echo      详见: DEPLOYMENT_GUIDE.md
    echo.
    pause
    exit /b 1
)

echo.
echo ════════════════════════════════════════════════════════════════
echo ✅ 推送成功！
echo ════════════════════════════════════════════════════════════════
echo.
echo 🎉 代码已成功推送到 GitHub！
echo.
echo 📍 你的仓库地址:
echo    https://github.com/%GITHUB_USERNAME%/%REPO_NAME%
echo.
echo 🔜 下一步操作:
echo.
echo    1️⃣  配置 GitHub Secrets（5 分钟）⭐ 重要！
echo       仓库页面 → Settings → Secrets and variables → Actions
echo       需要配置 4 个 Secrets:
echo          • ANTHROPIC_API_KEY: sk-WlhCHmgDcptriJCMM3oRYWSmVLPxQlcMVHF0iijBdNJSAJj5
echo          • ANTHROPIC_BASE_URL: https://yunwu.ai
echo          • ANTHROPIC_MODEL: claude-sonnet-4-5-20250929
echo          • TIANAPI_KEY: eda7b8c9c35234ce9a0dfd6939ae8c85
echo.
echo       详细步骤: 查看 YOUR_CONFIG_CHECKLIST.md
echo.
echo    2️⃣  手动触发首次运行（2 分钟）
echo       Actions → Weibo Trending Analysis → Run workflow
echo.
echo    3️⃣  下载分析报告
echo       Artifacts → 下载 HTML 文件
echo.
echo 📚 详细文档:
echo    - YOUR_CONFIG_CHECKLIST.md   (你的专属配置清单)
echo    - QUICK_START.md             (快速开始指南)
echo    - DEPLOYMENT_GUIDE.md        (完整部署教程)
echo.
echo ════════════════════════════════════════════════════════════════
echo.
pause
