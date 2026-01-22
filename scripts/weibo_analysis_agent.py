#!/usr/bin/env python3
"""
微博热搜产品创意分析 - Claude Agent SDK 版本
使用 Anthropic Claude API 实现自动化分析
支持第三方 API 端点（如 yunwu.ai 等）
"""

import os
import json
import requests
from datetime import datetime
from pathlib import Path
from anthropic import Anthropic

# 配置
TIANAPI_ENDPOINT = "https://apis.tianapi.com/weibohot/index"
MAX_TOPICS = int(os.getenv("MAX_TOPICS", "15"))
MIN_SCORE_EXCELLENT = 80
MIN_SCORE_GOOD = 60

# 第三方 API 配置（支持自定义端点）
ANTHROPIC_BASE_URL = os.getenv("ANTHROPIC_BASE_URL", None)  # 自定义 API 端点
ANTHROPIC_MODEL = os.getenv("ANTHROPIC_MODEL", "claude-3-5-sonnet-20241022")  # 自定义模型名称


def fetch_weibo_trends(api_key: str) -> list:
    """
    获取微博热搜数据
    """
    print("Fetching Weibo trending data...")

    try:
        response = requests.get(
            TIANAPI_ENDPOINT,
            params={"key": api_key},
            timeout=10
        )
        response.raise_for_status()
        data = response.json()

        if data.get("code") == 200:
            trends = data.get("result", {}).get("list", [])
            print(f"✅ 成功获取 {len(trends)} 条热搜话题")
            return trends
        else:
            print(f"❌ API 错误: {data.get('msg')}")
            return []

    except Exception as e:
        print(f"❌ 获取数据失败: {e}")
        return []


def analyze_trends_with_claude(trends: list, anthropic_api_key: str) -> dict:
    """
    使用 Claude API 分析热点并生成产品创意
    支持第三方 API 端点
    """
    # 创建客户端，支持自定义 base_url
    client_kwargs = {"api_key": anthropic_api_key}

    if ANTHROPIC_BASE_URL:
        client_kwargs["base_url"] = ANTHROPIC_BASE_URL
        print(f"Using custom API endpoint: {ANTHROPIC_BASE_URL}")

    client = Anthropic(**client_kwargs)

    # 准备分析数据
    trends_to_analyze = trends[:MAX_TOPICS]
    print(f"\nAnalyzing top {len(trends_to_analyze)} trends...\n")

    # 构建 prompt
    trends_text = "\n".join([
        f"{i+1}. {trend.get('hotword')} (热度: {trend.get('hotwordnum', 'N/A')})"
        for i, trend in enumerate(trends_to_analyze)
    ])

    prompt = f"""你是一位专业的产品分析师，擅长从社交媒体趋势中发现创新机会。

请分析以下微博热搜话题，为每个话题生成产品创意：

{trends_text}

对于每个话题，请执行以下步骤：

1. **背景研究**: 分析这个话题为什么热门，背后的社会/文化意义
2. **产品创意生成**: 生成 1-3 个可行的产品创意
3. **评分**: 基于以下标准打分（总分100分）
   - 有趣度 (80分): 病毒传播潜力 + 情感吸引力 + 社区参与度 + 文化相关性
   - 有用度 (20分): 问题解决潜力 + 市场需求

请以 JSON 格式返回分析结果，格式如下：

{{
  "analysis_date": "YYYY-MM-DD HH:MM:SS",
  "total_trends": 数量,
  "trends": [
    {{
      "rank": 1,
      "title": "话题标题",
      "heat_value": "热度值",
      "background": "背景分析（2-3句话）",
      "timeline": ["时间点1: 事件描述", "时间点2: 事件描述"],
      "product_ideas": [
        {{
          "name": "产品名称",
          "features": ["功能1", "功能2", "功能3"],
          "target_users": "目标用户画像",
          "innovation": "创新角度说明",
          "interest_score": 68,
          "utility_score": 18,
          "total_score": 86,
          "score_justification": "评分理由"
        }}
      ],
      "best_score": 86
    }}
  ]
}}

重要提示：
- 所有内容使用中文
- 评分要客观公正
- 产品创意要具有可行性
- 背景分析要基于常识和逻辑推理
- 只返回 JSON，不要其他文字说明
"""

    print(f"Calling Claude API for analysis...")
    print(f"Using model: {ANTHROPIC_MODEL}")
    print("This may take 1-2 minutes, please wait...\n")

    try:
        response = client.messages.create(
            model=ANTHROPIC_MODEL,
            max_tokens=16000,
            temperature=0.7,
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        )

        # 提取响应文本
        response_text = response.content[0].text

        # 清理可能的 markdown 代码块标记
        if response_text.startswith("```json"):
            response_text = response_text[7:]
        if response_text.startswith("```"):
            response_text = response_text[3:]
        if response_text.endswith("```"):
            response_text = response_text[:-3]

        # 解析 JSON
        analysis_result = json.loads(response_text.strip())

        print("✅ 分析完成！\n")

        # 打印统计信息
        excellent_count = sum(1 for t in analysis_result.get("trends", [])
                             if t.get("best_score", 0) >= MIN_SCORE_EXCELLENT)
        good_count = sum(1 for t in analysis_result.get("trends", [])
                        if MIN_SCORE_GOOD <= t.get("best_score", 0) < MIN_SCORE_EXCELLENT)
        total_ideas = sum(len(t.get("product_ideas", [])) for t in analysis_result.get("trends", []))

        print(f"Analysis Statistics:")
        print(f"   - 总计分析: {len(analysis_result.get('trends', []))} 个热点")
        print(f"   - 优秀创意 (≥{MIN_SCORE_EXCELLENT}分): {excellent_count} 个")
        print(f"   - 良好创意 ({MIN_SCORE_GOOD}-{MIN_SCORE_EXCELLENT-1}分): {good_count} 个")
        print(f"   - 产品创意总数: {total_ideas} 个\n")

        return analysis_result

    except json.JSONDecodeError as e:
        print(f"❌ JSON 解析失败: {e}")
        print(f"响应内容: {response_text[:500]}...")
        return {}
    except Exception as e:
        print(f"❌ Claude API 调用失败: {e}")
        return {}


def generate_html_report(analysis_data: dict) -> str:
    """
    生成 HTML 分析报告
    """
    print("Generating HTML report...")

    # 读取模板
    template_path = Path(__file__).parent.parent / ".claude" / "skills" / "weibo-trending-product-ideas" / "template.html"

    if template_path.exists():
        with open(template_path, "r", encoding="utf-8") as f:
            html_template = f.read()
    else:
        # 使用简化的内联模板
        html_template = """<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>微博热搜产品创意分析报告</title>
    <style>
        body { font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif; max-width: 1200px; margin: 0 auto; padding: 20px; background: #f5f5f5; }
        .header { background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); color: white; padding: 30px; border-radius: 10px; text-align: center; }
        .stats-bar { display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 20px; margin: 20px 0; }
        .stat-card { background: white; padding: 20px; border-radius: 10px; text-align: center; }
        .stat-number { font-size: 32px; font-weight: bold; color: #667eea; }
        .trend-item { background: white; border-radius: 10px; padding: 25px; margin: 20px 0; }
        .trend-item.excellent { border-left: 5px solid #10b981; }
        .trend-item.good { border-left: 5px solid #3b82f6; }
        .trend-item.normal { border-left: 5px solid #6b7280; }
        .score-badge { font-size: 28px; font-weight: bold; padding: 10px 20px; border-radius: 8px; display: inline-block; }
        .score-excellent { background: #d1fae5; color: #065f46; }
        .score-good { background: #dbeafe; color: #1e40af; }
        .score-normal { background: #f3f4f6; color: #374151; }
        .product-idea { background: #fef3c7; padding: 20px; border-radius: 8px; margin: 15px 0; border: 2px solid #fbbf24; }
        .product-name { font-size: 20px; font-weight: bold; color: #92400e; margin-bottom: 10px; }
    </style>
</head>
<body>
    <div class="header">
        <h1>📊 微博热搜产品创意分析报告</h1>
        <p>生成时间: {CURRENT_DATE}</p>
    </div>
    {STATS_BAR}
    {TREND_ITEMS}
    <div style="text-align: center; margin-top: 40px; color: #6b7280;">
        🤖 Powered by Claude API | AI赋能产品创新
    </div>
</body>
</html>"""

    # 生成统计信息
    trends = analysis_data.get("trends", [])
    excellent_count = sum(1 for t in trends if t.get("best_score", 0) >= MIN_SCORE_EXCELLENT)
    good_count = sum(1 for t in trends if MIN_SCORE_GOOD <= t.get("best_score", 0) < MIN_SCORE_EXCELLENT)
    total_ideas = sum(len(t.get("product_ideas", [])) for t in trends)

    stats_html = f"""
    <div class="stats-bar">
        <div class="stat-card">
            <div class="stat-number">{len(trends)}</div>
            <div class="stat-label">分析热点数量</div>
        </div>
        <div class="stat-card">
            <div class="stat-number">{excellent_count}</div>
            <div class="stat-label">优秀创意 (≥{MIN_SCORE_EXCELLENT}分)</div>
        </div>
        <div class="stat-card">
            <div class="stat-number">{good_count}</div>
            <div class="stat-label">良好创意 ({MIN_SCORE_GOOD}-{MIN_SCORE_EXCELLENT-1}分)</div>
        </div>
        <div class="stat-card">
            <div class="stat-number">{total_ideas}</div>
            <div class="stat-label">产品创意总数</div>
        </div>
    </div>
    """

    # 按评分排序
    sorted_trends = sorted(trends, key=lambda x: x.get("best_score", 0), reverse=True)

    # 生成每个热点的 HTML
    trend_items_html = ""
    for trend in sorted_trends:
        score = trend.get("best_score", 0)

        # 确定分级
        if score >= MIN_SCORE_EXCELLENT:
            grade_class = "excellent"
            score_class = "score-excellent"
        elif score >= MIN_SCORE_GOOD:
            grade_class = "good"
            score_class = "score-good"
        else:
            grade_class = "normal"
            score_class = "score-normal"

        # 生成产品创意 HTML
        ideas_html = ""
        for idea in trend.get("product_ideas", []):
            features_html = "<br>".join([f"• {f}" for f in idea.get("features", [])])

            ideas_html += f"""
            <div class="product-idea">
                <div class="product-name">💡 {idea.get('name', '未命名')}</div>
                <div><strong>核心功能:</strong><br>{features_html}</div>
                <div><strong>目标用户:</strong> {idea.get('target_users', 'N/A')}</div>
                <div><strong>创新角度:</strong> {idea.get('innovation', 'N/A')}</div>
                <div><strong>评分:</strong> 有趣度 {idea.get('interest_score', 0)}/80 | 有用度 {idea.get('utility_score', 0)}/20 | 综合 {idea.get('total_score', 0)}/100</div>
            </div>
            """

        # 生成时间线
        timeline_html = "<br>".join([f"• {item}" for item in trend.get("timeline", [])])

        trend_items_html += f"""
        <div class="trend-item {grade_class}">
            <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 20px;">
                <div>
                    <h2>#{trend.get('rank', '?')} {trend.get('title', '未知话题')}</h2>
                    <div style="color: #6b7280;">🔥 热度: {trend.get('heat_value', 'N/A')}</div>
                </div>
                <div class="score-badge {score_class}">{score}<br><small>/100</small></div>
            </div>
            <div>
                <h3>📅 事件时间线</h3>
                <div style="background: #f9fafb; padding: 15px; border-radius: 8px;">
                    {timeline_html if timeline_html else '暂无时间线信息'}
                </div>
            </div>
            <div>
                <h3>🔍 背景分析</h3>
                <div style="background: #f0f9ff; padding: 15px; border-radius: 8px;">
                    {trend.get('background', '暂无背景分析')}
                </div>
            </div>
            <div>
                <h3>💡 产品创意</h3>
                {ideas_html if ideas_html else '<p>暂无产品创意</p>'}
            </div>
        </div>
        """

    # 替换模板变量
    current_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    html_content = html_template.replace("{CURRENT_DATE}", current_date)
    html_content = html_content.replace("{STATS_BAR}", stats_html)
    html_content = html_content.replace("{TREND_ITEMS}", trend_items_html)
    html_content = html_content.replace("{TOTAL_TRENDS}", str(len(trends)))
    html_content = html_content.replace("{EXCELLENT_COUNT}", str(excellent_count))
    html_content = html_content.replace("{GOOD_COUNT}", str(good_count))
    html_content = html_content.replace("{TOTAL_IDEAS}", str(total_ideas))

    return html_content


def main():
    """
    主函数
    """
    print("=" * 60)
    print("Weibo Trending Analysis - GitHub Actions Version")
    print("=" * 60)
    print()

    # 获取环境变量
    anthropic_api_key = os.getenv("ANTHROPIC_API_KEY")
    tianapi_key = os.getenv("TIANAPI_KEY")

    if not anthropic_api_key:
        print("❌ 错误: 未设置 ANTHROPIC_API_KEY 环境变量")
        return 1

    if not tianapi_key:
        print("❌ 错误: 未设置 TIANAPI_KEY 环境变量")
        return 1

    # Step 1: 获取微博热搜
    trends = fetch_weibo_trends(tianapi_key)
    if not trends:
        print("❌ 无法获取微博热搜数据，退出")
        return 1

    # Step 2: 使用 Claude 分析
    analysis_result = analyze_trends_with_claude(trends, anthropic_api_key)
    if not analysis_result:
        print("❌ 分析失败，退出")
        return 1

    # Step 3: 生成 HTML 报告
    html_content = generate_html_report(analysis_result)

    # 保存报告
    reports_dir = Path("reports")
    reports_dir.mkdir(exist_ok=True)

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    report_path = reports_dir / f"weibo_trending_analysis_{timestamp}.html"

    with open(report_path, "w", encoding="utf-8") as f:
        f.write(html_content)

    print(f"✅ HTML 报告已生成: {report_path}")

    # 创建 latest.html 链接（用于 GitHub Pages）
    latest_path = reports_dir / "latest.html"
    try:
        import shutil
        shutil.copy2(report_path, latest_path)
        print(f"✅ 最新报告链接已创建: {latest_path}")
    except Exception as e:
        print(f"⚠️  创建 latest.html 失败: {e}")

    print()
    print("=" * 60)
    print("✨ 分析完成！")
    print("=" * 60)

    return 0


if __name__ == "__main__":
    exit(main())
