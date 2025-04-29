import requests
from bs4 import BeautifulSoup
import csv
import json
import time
import re

soup = BeautifulSoup()

with open("test.html", "r", encoding="utf-8") as f:
    soup = BeautifulSoup(f, "html.parser")

i = 10
for a in soup.find_all("a",target="_blank",href=re.compile("(\/\/)?(www\.)?bilibili\.com\/video\/BV[a-zA-Z0-9]{10}(\/|\?.*)?")):
    title_tag = a.find("img",alt=True)
    if title_tag:
        title = title_tag["alt"]
    else:
        continue
    print("https:"+a["href"],end = " : ")
    print("《"+title+"》")
    i = i - 1
    if i == 0:
        break