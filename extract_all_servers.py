import json
import sys
import re

sys.stdout.reconfigure(encoding='utf-8')

# 读取JSON文件
json_file = r'C:\Users\admin\.claude\projects\C--Users-admin-Desktop-----skill\ff8d7b6f-0002-4ff6-823a-bb5cc4197221\tool-results\toolu_01Hx1wN7BsdCU3J4Vg6E1EJg.json'
data = json.load(open(json_file, 'r', encoding='utf-8'))

# 提取Result部分
text = data[0]['text']
match = re.search(r'### Result\s*(\{.*?\})\s*### Ran', text, re.DOTALL)
result_json = match.group(1) if match else '{}'
parsed = json.loads(result_json)

# 获取archived内容（包含第三方服务器）
archived_content = parsed.get('archived', '')

# 找到第三方服务器部分
third_party_start = archived_content.find('Official Integrations')
if third_party_start == -1:
    print("未找到第三方服务器部分")
    sys.exit(1)

third_party_content = archived_content[third_party_start:]
lines = third_party_content.split('\n')

# 输出所有第三方服务器
print("# 所有第三方MCP服务器详细列表\n")
print("从GitHub仓库 https://github.com/modelcontextprotocol/servers 提取\n")
print("---\n")

count = 0
for line in lines:
    line = line.strip()

    # 跳过标题、注释和空行
    if not line:
        continue
    if line.startswith('Official Integrations'):
        continue
    if line.startswith('Note'):
        continue
    if 'server lists in this README' in line:
        continue
    if line.startswith('The following'):
        continue

    # 处理服务器条目（包含 " - " 分隔符）
    if ' - ' in line:
        # 移除可能的emoji和特殊字符
        clean_line = re.sub(r'^[\U0001F300-\U0001F9FF\s\u2800-\u28FF]+', '', line)

        count += 1
        parts = clean_line.split(' - ', 1)
        if len(parts) == 2:
            name = parts[0].strip()
            description = parts[1].strip()
            print(f"### {count}. {name}")
            print(f"**功能描述**: {description}\n")

print(f"\n---\n\n**总计**: {count} 个第三方MCP服务器")
