#!/usr/bin/python
# -*- coding: UTF-8 -*-
import requests

# Cloudflare API相关信息
API_TOKEN = ""
ZONE_ID = ""
RECORD_ID = ""


# 获取ipv6地址
def getIPv6Address():
    text = requests.get('https://v6.ident.me').text
    return text


# 更新的IPv6地址
NEW_IPV6_ADDRESS = getIPv6Address()

# 构建API请求的URL
url = f"https://api.cloudflare.com/client/v4/zones/{ZONE_ID}/dns_records/{RECORD_ID}"

# 构建请求头
headers = {
    "Authorization": f"Bearer {API_TOKEN}",
    "Content-Type": "application/json"
}

# 构建请求体数据
data = {
    "type": "AAAA",
    "name": "",  # 替换为你的域名
    "content": NEW_IPV6_ADDRESS,
    "ttl": 120,
    "proxied": False
}

# 发送PUT请求来更新记录
response = requests.put(url, json=data, headers=headers)

# 处理响应
if response.status_code == 200:
    print("AAAA记录已更新成功！")
else:
    print("AAAA记录更新失败。HTTP响应码:", response.status_code)
    print("响应内容:", response.text)
