# -*- coding: UTF-8 -*-
'''
@Project ：nphRS4 
@File    ：fangdi.py
@IDE     ：PyCharm 
@Author  ：ning
@Date    ：2024-06-11 14:06 
'''

import re
from lxml import etree
import execjs
import requests
from parsel import Selector

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36",
    "Accept": "application/json, text/javascript, */*; q=0.01",
    "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
    "Cache-Control": "no-cache",
    "Connection": "keep-alive",
    "Content-Type": "application/x-www-form-urlencoded;charset=UTF-8",
    "Origin": "http://www.fangdi.com.cn",
    "Pragma": "no-cache",
    "Referer": "http://www.fangdi.com.cn/",
}
url = "http://www.fangdi.com.cn/"
response = requests.get(url, headers=headers, verify=False)
with open('./fangdi.html', 'w', encoding='utf8') as f:
    f.write(response.text)

# 获取cookie
ic = response.cookies.get("www.fangdi.com_http_ic")
S80 = response.cookies.get("FSSBBIl1UgzbN7N80S")
JSESSIONID1 = response.cookies.get("JSESSIONID1")
cn = response.cookies.get("www.fangdi.com.cn")
# print(f"80S：{S80}")


etree_html = etree.HTML(response.text)
content = etree_html.xpath("//meta/@content")[-1]
script = etree_html.xpath("//script")
js_url = 'http://www.fangdi.com.cn' + script[0].xpath("@src")[0]
resp = requests.get(js_url, headers=headers)

js_content = '''var content="contentfff";'''.replace("contentfff", content)
js_dfe1657 = resp.text
js_auto_code = script[1].xpath("text()")[0]
get_cookie_url = """
function get_cookie_url(){
    window.XMLHttpRequest.prototype.open('GET', './modules/top.jsp', false)
    return {
        'cookie': document.cookie,
        'url': window.xhr_url['1']
    };
}
"""
with open("fangdi.js", encoding='utf-8') as f:
    js_env_code = f.read()
run_code = js_content + ";" + "\r\n" + js_env_code + ";" + "\r\n" + js_dfe1657 + ";" + "\r\n" + "\r\n" + "debugger;" + js_auto_code + ";" + "\r\n" + get_cookie_url + "\r\n"

with open('./fangdi_run_coder.js', 'w', encoding='utf8') as f:
    f.write(run_code)

ru = execjs.compile(run_code)

result = ru.call("get_cookie_url")
url = result['url']
cookie = result['cookie'].split("=")[1].split(";")[0]

print(f"生成的result：{result}")

# 防止滥用，发包逻辑已删除