#!/usr/bin/env python3
"""
微博热搜监控脚本
演示 Claude Code 后台命令功能
"""
import time
import json
from datetime import datetime
import os

def fetch_weibo_trends():
    """模拟获取微博热搜数据"""
    # 这里使用模拟数据，实际应该调用 API
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    trends = {
        "timestamp": timestamp,
        "热搜": [
            {"rank": 1, "title": "示例热搜1", "heat": 5000000},
            {"rank": 2, "title": "示例热搜2", "heat": 3000000},
            {"rank": 3, "title": "示例热搜3", "heat": 2000000},
        ]
    }
    return trends

def save_to_file(data, filename="weibo_monitor_log.jsonl"):
    """追加保存数据到文件"""
    with open(filename, "a", encoding="utf-8") as f:
        f.write(json.dumps(data, ensure_ascii=False) + "\n")

def monitor(interval_minutes=60, max_runs=None):
    """
    持续监控微博热搜

    Args:
        interval_minutes: 监控间隔（分钟）
        max_runs: 最大运行次数，None 表示无限运行
    """
    run_count = 0
    print(f"[START] 微博热搜监控启动")
    print(f"[INFO] 监控间隔: {interval_minutes} 分钟")
    print(f"[INFO] 日志文件: weibo_monitor_log.jsonl")
    print("-" * 50)

    try:
        while True:
            run_count += 1
            print(f"\n[第 {run_count} 次采集] {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

            # 获取数据
            trends = fetch_weibo_trends()

            # 保存数据
            save_to_file(trends)

            # 显示前3条
            for item in trends["热搜"][:3]:
                print(f"  {item['rank']}. {item['title']} (热度: {item['heat']:,})")

            # 检查是否达到最大运行次数
            if max_runs and run_count >= max_runs:
                print(f"\n[DONE] 已完成 {max_runs} 次采集，监控结束")
                break

            # 等待下一次采集
            print(f"[WAIT] 等待 {interval_minutes} 分钟后进行下一次采集...")
            time.sleep(interval_minutes * 60)

    except KeyboardInterrupt:
        print(f"\n\n[STOP] 监控被手动停止")
        print(f"[STAT] 总共采集了 {run_count} 次")

if __name__ == "__main__":
    # 演示模式：每1分钟采集一次，共采集3次
    # 实际使用：修改为 monitor(interval_minutes=60, max_runs=None) 实现7x24小时监控
    monitor(interval_minutes=1, max_runs=3)
