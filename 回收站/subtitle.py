import requests

video_url = "https://www.bilibili.com/video/BV1xx411x7xx"  # 替换为目标视频链接
subtitle_api_url = "https://aisubtitle.hdslb.com/bfs/subtitle/...json"  # 捕获到的实际API地址

headers = {
    "User-Agent": "Mozilla/5.0",
    "Referer": video_url  # 必须包含Referer以通过B站反爬
}

response = requests.get(subtitle_api_url, headers=headers)
if response.status_code == 200:
    subtitle_data = response.json()
    print(subtitle_data)  # 直接获取JSON格式字幕内容
    # 7c088202f6e047b75b18fd4cd2b52b2c34cd3eb7.json?auth_key=1746095734-b5f417891e4446259ef3e91cb004d63c-0-72cb07777b78a2a7c9d15735da3f5a65
    # 7c088202f6e047b75b18fd4cd2b52b2c34cd3eb7.json?auth_key=1746090004-bd194263ea5346839bdfe97de0c7deb3-0-62213ed670eec3ab0ba687102d7fec98