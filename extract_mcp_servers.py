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

# 获取reference和archived内容
reference_content = parsed.get('reference', '')
archived_content = parsed.get('archived', '')

print("=" * 80)
print("MCP服务器完整列表")
print("=" * 80)

print("\n" + "=" * 80)
print("一、参考服务器 (Reference Servers)")
print("=" * 80)

# 处理Reference Servers
ref_lines = reference_content.split('\n')
ref_count = 0
for line in ref_lines:
    line = line.strip()
    if line and ' - ' in line and not line.startswith('These'):
        ref_count += 1
        print(f"\n{ref_count}. {line}")

print("\n" + "=" * 80)
print("二、已归档服务器 (Archived Servers)")
print("=" * 80)

# 提取Archived部分
archived_lines = archived_content.split('\n')
arch_count = 0
for line in archived_lines:
    line = line.strip()
    if line and ' - ' in line:
        # 只处理Archived部分的服务器
        if 'Official Integrations' in archived_content[:archived_content.index(line) if line in archived_content else 0]:
            break
        arch_count += 1
        print(f"\n{arch_count}. {line}")

print("\n" + "=" * 80)
print("三、第三方服务器 (Third-Party Servers)")
print("=" * 80)

# 提取Third-Party部分
third_party_start = archived_content.find('Official Integrations')
if third_party_start != -1:
    third_party_content = archived_content[third_party_start:]
    tp_lines = third_party_content.split('\n')
    tp_count = 0

    for line in tp_lines:
        line = line.strip()
        # 跳过标题和注释行
        if line and ' - ' in line and not line.startswith('Official') and not line.startswith('Note'):
            tp_count += 1
            # 移除可能的emoji符号
            clean_line = re.sub(r'^[\U0001F300-\U0001F9FF\s]+', '', line)
            print(f"\n{tp_count}. {clean_line}")

print("\n" + "=" * 80)
print(f"总计: {ref_count} 个参考服务器 + {arch_count} 个已归档服务器 + {tp_count} 个第三方服务器")
print("=" * 80)
