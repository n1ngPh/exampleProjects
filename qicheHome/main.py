# -*- coding: UTF-8 -*-
import execjs
import requests
import re

URL = 'https://car.autohome.com.cn/config/series/6261.html'

ctx = execjs.compile(open('part.js', encoding='utf-8').read())
rulePosList = ctx.call("get_rulePosList")
ruleDict = ctx.call("get_ruleDict")

# rulePosList[1].split(",")[0]

def func(obj):
    word = ''
    num = re.findall('(\d+)', obj.group(0))[0]
    temp = rulePosList[int(num)].split(",")
    for i in temp:
        word += ruleDict[int(i)]
    return word

def htmlReplace(html):
    responseReplace = re.sub("<span class='hs_kw\d+_config\w+'></span>", func, html)
    return responseReplace

def main():
    heaters = {
    }
    response = requests.get(url=URL, headers=heaters).text
    html = htmlReplace(response)
    config = re.findall('var config = (.*?)};', html)
    print(config)

main()




