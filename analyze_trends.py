#!/usr/bin/env python3
"""
微博热搜数据分析脚本
演示 Subagent 的使用场景
"""
import json
from collections import Counter
from datetime import datetime

def load_monitor_data(filename="weibo_monitor_log.jsonl"):
    """加载监控日志数据"""
    data = []
    try:
        with open(filename, "r", encoding="utf-8") as f:
            for line in f:
                data.append(json.loads(line.strip()))
    except FileNotFoundError:
        print(f"⚠️  文件 {filename} 不存在")
        return []
    return data

def analyze_trends(data):
    """分析热搜趋势"""
    if not data:
        return None

    # 统计所有出现的热搜标题
    all_titles = []
    for record in data:
        for item in record.get("热搜", []):
            all_titles.append(item["title"])

    # 找出最频繁出现的热搜
    title_counts = Counter(all_titles)

    analysis = {
        "总采集次数": len(data),
        "采集时间范围": {
            "开始": data[0]["timestamp"] if data else None,
            "结束": data[-1]["timestamp"] if data else None,
        },
        "热搜频次排行": title_counts.most_common(10),
        "独立热搜数量": len(title_counts),
    }

    return analysis

def print_analysis(analysis):
    """打印分析结果"""
    if not analysis:
        print("❌ 没有数据可分析")
        return

    print("\n" + "="*60)
    print("📊 微博热搜数据分析报告")
    print("="*60)

    print(f"\n📈 基本统计:")
    print(f"  • 总采集次数: {analysis['总采集次数']}")
    print(f"  • 独立热搜数: {analysis['独立热搜数量']}")
    print(f"  • 时间范围: {analysis['采集时间范围']['开始']} ~ {analysis['采集时间范围']['结束']}")

    print(f"\n🔥 热搜频次 TOP 10:")
    for i, (title, count) in enumerate(analysis['热搜频次排行'], 1):
        print(f"  {i:2d}. {title} (出现 {count} 次)")

    print("\n" + "="*60)

if __name__ == "__main__":
    print("🔍 开始分析微博热搜数据...\n")

    # 加载数据
    data = load_monitor_data()

    # 分析数据
    analysis = analyze_trends(data)

    # 打印结果
    print_analysis(analysis)
