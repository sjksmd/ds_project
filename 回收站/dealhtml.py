import re
from html.parser import HTMLParser

urlnum = 10  # 需要收集的条目数

class BilibiliParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.result = ''
        self.current_href = None
        self.href_pattern = re.compile(r'^(\/\/)?(www\.)?bilibili\.com\/video\/BV[a-zA-Z0-9]{10}(\/|\?.*)?$')
        self.remaining = urlnum
        self.in_target_a = False  # 是否在目标a标签内
        self.current_alt = None   # 当前找到的alt属性

    def handle_starttag(self, tag, attrs):
        if self.remaining <= 0:
            return

        # 将属性转换为字典（小写键）
        attrs = {k.lower(): v for k, v in attrs}
        
        # 检查是否为target="_blank"的a标签
        if tag == 'a' and attrs.get('target') == '_blank':
            href = attrs.get('href', '')
            if href and self.href_pattern.match(href):
                self.in_target_a = True
                self.current_href = href
                self.current_alt = None  # 重置alt

        # 在目标a标签内搜索带alt的img标签
        elif tag == 'img' and self.in_target_a and not self.current_alt:
            if 'alt' in attrs:
                self.current_alt = attrs['alt']

    def handle_endtag(self, tag):
        if tag == 'a' and self.in_target_a:
            self.in_target_a = False
            if self.current_href and self.current_alt and self.remaining > 0:
                # 构造完整URL并存储结果
                full_url = f'https:{self.current_href}'
                # self.result[full_url] = self.current_alt
                self.result += f'{full_url}:{self.current_alt}\n'
                self.remaining -= 1

            # 重置临时变量
            self.current_href = None
            self.current_alt = None
async def main(args: Args)->Output:
    html = args.params['input']
    parser = BilibiliParser()
    parser.feed(html)
    ret = parser.result 
    return ret