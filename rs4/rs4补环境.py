import re
from lxml import etree
import execjs
import requests
from parsel import Selector

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36"
}
url = "https://hd.ghzyj.sh.gov.cn/2017/xxgk/zcjd/"
response = requests.get(url, headers=headers, verify=False)
with open('./zcjd.html', 'w', encoding='utf8') as f:
    f.write(response.text)
ic = response.cookies.get("hd.ghzyj.sh.gov.cn_443_ic")  # 获取cookie
S80 = response.cookies.get("FSSBBIl1UgzbN7N443S")  # 获取cookie
print(f"80S：{S80}")
etree_html = etree.HTML(response.text)
content = etree_html.xpath("//meta/@content")[1]
print(f"content：{content}")
script = etree_html.xpath("//script")
js_url = 'https://hd.ghzyj.sh.gov.cn' + script[0].xpath("@src")[0]
resp = requests.get(js_url, headers=headers)
js_content = '''var content="contentfff";'''.replace("contentfff", content)
js_dfe1657 = resp.text
js_auto_code = script[1].xpath("text()")[0]
get_cookie = """
function get_cookie(){
    return document.cookie;
}
"""
with open("rs4补环境.js", encoding='utf-8') as f:
    js_env_code = f.read()
run_code = js_content + ";" + "\r\n" + js_env_code + ";" + "\r\n" + js_dfe1657 + ";" + "\r\n" + "\r\n" + "debugger;" + js_auto_code + ";" + "\r\n" + get_cookie + "\r\n"

with open('./run_coder.js', 'w', encoding='utf8') as f:
    f.write(run_code)

ru = execjs.compile(run_code)

cookie = ru.call("get_cookie").split("=")[1].split(";")[0]
print(f"生成的cookie：{cookie}")
# 防止滥用，发包逻辑已删除