import re

# URL 正则表达式


def is_valid_url(url):
    url_regex = re.compile(
        r'^(https?|ftp):\/\/'  # 协议 http, https, ftp
        r'([a-zA-Z0-9.-]+)'    # 域名
        r'(:[0-9]{1,5})?'      # 端口号（可选）
        r'(\/.*)?$'            # 路径（可选）
    )
    if re.match(url_regex, url) is not None:
        return 1
    else:
        return 0

# 测试示例
urls = [
    "https://www.example.com/path",
    "ftp://example.com/resource",
    "http://localhost:8000",
    "www.example.com",  # 缺少协议
    "http://",          # 不完整
    "https://123.456.789.000"  # 不合法的 IP
]

for url in urls:
    print(f"{url} -> {is_valid_url(url)}")