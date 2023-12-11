import requests

# 替换为您的Cloudflare API令牌、域名Zone ID和DNS记录名称
api_token = 'your_api_token'
zone_id = 'your_zone_id'
record_name = 'your_record_name'

# 设置Cloudflare API的URL
url = f'https://api.cloudflare.com/client/v4/zones/{zone_id}/dns_records'

# 设置请求头，包括身份验证信息
headers = {
    'Authorization': f'Bearer {api_token}',
    'Content-Type': 'application/json',
}

# 发送GET请求以获取DNS记录列表
response = requests.get(url, headers=headers)

# 检查响应是否成功
if response.status_code == 200:
    data = response.json()
    # 寻找匹配的DNS记录并获取其Record ID
    for record in data['result']:
        if record['name'] == record_name:
            record_id = record['id']
            print(f"DNS记录名称: {record_name}, Record ID: {record_id}")
            break
    else:
        print(f"未找到名为 {record_name} 的DNS记录")
else:
    print(f"请求失败，状态码: {response.status_code}")