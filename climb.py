import requests
from bs4 import BeautifulSoup
import csv
import json
import time

url = 'https://search.bilibili.com/all?vt=13417376&keyword=%E9%BC%A0%E6%A0%87&from_source=webtop_search&spm_id_from=333.1007&search_source=5'
headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36 Edg/135.0.0.0',
            'Accept-Language': 'zh-CN,zh;q=0.9'
        }
params = None
html = ''

try:
    response = requests.get(
        url = url,
        headers=headers,
        params=params,
        timeout=10
    )
    response.raise_for_status()  # 检查HTTP错误
    response.encoding = response.apparent_encoding  # 自动识别编码
    html = response.text
except requests.exceptions.RequestException as e:
    print(f"请求失败: {e}")
    html = None

soup = BeautifulSoup(html, 'html.parser')
  
with open('test.html', 'w', encoding='utf-8') as f:
    f.write(soup.prettify())

    