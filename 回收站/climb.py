import requests
from bs4 import BeautifulSoup
import csv
import json
import time

url = 'https://www.bilibili.com/video/BV16G4y1S7Hp/'
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
  
with open('video.html', 'w', encoding='utf-8') as f:
    f.write(soup.prettify())

    