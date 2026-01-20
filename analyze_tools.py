import json

# 读取文件
file_path = r'C:\Users\admin\.claude\projects\C--Users-admin-Desktop-----skill\0ebcce4e-35e2-4446-88a9-c6e877a7ac2f\tool-results\toolu_01XeQKguGFurdkA7nLqfnXkW.json'

with open(file_path, 'r', encoding='utf-8') as f:
    data = json.load(f)

# 提取文本内容
text = data[0]['text']

# 提取 "### Result\n" 后面的 JSON 字符串
json_start = text.find('### Result\n"') + len('### Result\n"')
json_end = text.rfind('"')
json_str = text[json_start:json_end]

# 解码 JSON 转义字符
json_str = json_str.replace('\\"', '"').replace('\\/', '/')

# 解析 JSON
api_data = json.loads(json_str)

# 筛选符合条件的工具
results = []
for tool in api_data['data']['data']:
    visits = tool['month_visited_count']
    growth = tool['growth']

    # 访问量在100万-300万之间，月度增长超过50万
    if 1000000 <= visits <= 3000000 and growth > 500000:
        results.append(tool)

# 输出结果
print(f'Total matching tools: {len(results)}\n')
print('='*80)
for i, tool in enumerate(results, 1):
    print(f'\n{i}. {tool["name"]}')
    print(f'   Visits: {tool["month_visited_count"]:,}')
    print(f'   Monthly Growth: {tool["growth"]:,}')
    print(f'   Growth Rate: {tool["growth_rate"]:.2%}')
    print(f'   Description: {tool["description"]}')
print('\n' + '='*80)
