import requests
from bs4 import BeautifulSoup
import re


async def main(args: Args) -> Output:
'''
    text = args.params['input']

    url = 'https://search.bilibili.com/all?vt=13417376&keyword='+text
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
'''
    soup = BeautifulSoup(html, 'html.parser')

    ret = dict()


    i = 10
    for a in soup.find_all("a",target="_blank",href=re.compile("(\/\/)?(www\.)?bilibili\.com\/video\/BV[a-zA-Z0-9]{10}(\/|\?.*)?")):
        title_tag = a.find("img",alt=True)
        if title_tag:
            title = title_tag["alt"]
        else:
            continue

        ret.update({"https:"+a["href"]:title})

        i = i - 1
        if i == 0:
            break

    return ret
