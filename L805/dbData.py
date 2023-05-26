# -*- coding:utf-8 -*-
# @Time : 2022/4/20 18:01
# @File : dbData.py
# @Software : PyCharm

import re
import random
import requests
from bs4 import BeautifulSoup
import getHTML
import jieba
from fake_useragent import UserAgent
import asyncio
import aiohttp
import gotoMySQL
import nest_asyncio

"""
获取豆瓣top250数据，保存到MySQL
"""


# 随机headers
def user_agrnt_random():
    user_agent_list = [
        "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; AcooBrowser; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
        "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0; Acoo Browser; SLCC1; .NET CLR 2.0.50727; Media Center PC 5.0; .NET CLR 3.0.04506)",
        "Mozilla/4.0 (compatible; MSIE 7.0; AOL 9.5; AOLBuild 4337.35; Windows NT 5.1; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
        "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0; Acoo Browser; SLCC1; .NET CLR 2.0.50727; Media Center PC 5.0; .NET CLR 3.0.04506)",
        "Mozilla/4.0 (compatible; MSIE 7.0; AOL 9.5; AOLBuild 4337.35; Windows NT 5.1; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
        "Mozilla/5.0 (Windows; U; MSIE 9.0; Windows NT 9.0; en-US)",
        "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 2.0.50727; Media Center PC 6.0)",
        "Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 1.0.3705; .NET CLR 1.1.4322)",
        "Mozilla/4.0 (compatible; MSIE 7.0b; Windows NT 5.2; .NET CLR 1.1.4322; .NET CLR 2.0.50727; InfoPath.2; .NET CLR 3.0.04506.30)",
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN) AppleWebKit/523.15 (KHTML, like Gecko, Safari/419.3) Arora/0.3 (Change: 287 c9dfb30)",
        "Mozilla/5.0 (X11; U; Linux; en-US) AppleWebKit/527+ (KHTML, like Gecko, Safari/419.3) Arora/0.6",
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.2pre) Gecko/20070215 K-Ninja/2.1.1",
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN; rv:1.9) Gecko/20080705 Firefox/3.0 Kapiko/3.0",
        "Mozilla/5.0 (X11; Linux i686; U;) Gecko/20070322 Kazehakase/0.4.5",
        "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.8) Gecko Fedora/1.9.0.8-1.fc10 Kazehakase/0.5.6",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_3) AppleWebKit/535.20 (KHTML, like Gecko) Chrome/19.0.1036.7 Safari/535.20",
        ]
    headers = {'User-agent': random.choice(user_agent_list)}
    return headers

# cookie字符串转化为字典
def convert_cookies_to_dict(cookies):
    cookies = dict([l.split("=", 1) for l in cookies.split("; ")])
    return cookies

def getResponds(url):
    # cookies = ' '
    # cookies = convert_cookies_to_dict(cookies)
    headers = user_agrnt_random()
    responds = requests.get(url=url, headers=headers)
    return responds

def getdbData():
    mysql = gotoMySQL.GotoMySQL(1)
    for i in range(0, 100, 25):
        url = 'https://movie.douban.com/top250?start={}&filter='.format(str(i))
        res = getResponds(url)
        film = res.text
        soup = BeautifulSoup(film, 'html.parser')
        items = soup.find_all(class_="item")

        for item in items:
            title = item.find(class_="title").text  # 电影名称
            pingfen = item.find(class_="rating_num").text  # 评分
            comment = item.find(class_="inq").text  # 短评
            link = item.find('a')['href']  # 网址
            token = link.split('/')[-2]     # 电影唯一编号
            arr = str(item.find(class_='bd'))
            arr = re.findall("(?s)<br/>(.*?)</p>", arr)[0].replace('\n', '').replace(r'\xa0/\xa0', '\\').replace(' ', '')  # 时间、地区、类型
            img = str(item.find(class_='pic'))
            img = re.findall('src="(.*?)"', img)[0]  # 电影海报连接

            respond = getResponds(link).text
            synopsis = re.findall('(?s)<span property="v:summary"(.*?)</span>', respond)[0].replace(" ", '').replace(
                "\n", '').replace("\u3000", '')     # 简介
            print(f"<{title}>加载完成")

            # 导入数据库
            mysql.writeMysql(token, title, pingfen, comment, link, img, arr, synopsis)

    # 关闭与数据库的连接
    mysql.close()


# 二级页面的图标数据
class Visu():
    def __init__(self):
        # 统计单词频率
        self.wordPL = {}
        # 评论数据
        self.commentData = []

    def getCommentData(self, token):
        self.token = token
        nest_asyncio.apply()
        loop = asyncio.get_event_loop()
        loop.run_until_complete(self.saveCommentData())

        return self.commentData, self.wordPL

    # 获得电影评论的url，异步爬取评论数据
    async def saveCommentData(self):
        tasks = []
        # ua = UserAgent()
        headers = {'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.64 Safari/537.36 Edg/101.0.1210.53"}
        async with aiohttp.ClientSession() as session:
            for i in range(20):
                # 一页有20条评论，url步进是20
                commentURL = f'https://movie.douban.com/subject/{self.token}/comments?start={int(i) * 20}'
                task = asyncio.create_task(self.fenxiCommentData(commentURL, session, headers))
                tasks.append(task)
            await asyncio.wait(tasks)

    async def fenxiCommentData(self, commentURL, session, headers):
        async with session.get(commentURL, headers=headers) as resp:
            html = await resp.text()
            for oneUser in re.findall('(?s)<div class="comment-item "(.*?)</p>', html):
                try:
                    userData = {}
                    short = re.findall('(?s)<span class="short">(.*?)</span>', oneUser)[0]
                    date = re.findall('comment-time " title="(.*?)">', oneUser)[0]
                    pingfen = re.findall('<span class="allstar(.*?) rating', oneUser)[0]

                    name = re.findall('class="">(.*?)</a>', oneUser)[0]
                    touxiang = re.findall('<img src="(.*?)"', oneUser)[0]
                    num = re.findall('class="votes vote-count">(.*?)</span>', oneUser)[0]

                    # 每获得一条评论，就调用countWord统计信息
                    # mark = 情感分析.sentiment_score(short)
                    self.countWord(short)
                    userData.update({'评星': pingfen, '日期': date, '简介': short, '昵称': name, '头像': touxiang, '点赞数': num})
                    self.commentData.append(userData)
                except:
                    print("")

    # 统计单词的频率
    def countWord(self, data):
        # 数据预处理，除去无关符号
        new_data = re.findall('[\u4e00-\u9fa5]+', data, re.S)
        new_data = "".join(new_data)
        words = jieba.lcut(new_data)
        # 可以设置停用单词
        stop_words = ['一个', '只有', '以及', '一天', '电影', '一部', '片子', '有点', '这么', '为了', '还是']
        # 统计单词频率
        for word in words:
            if word not in stop_words and len(word) > 1:
                if word in self.wordPL:
                    self.wordPL[f"{word}"] += 1
                else:
                    self.wordPL[f"{word}"] = 1



def main():
    # 获得豆瓣数据,导入到数据库
    getdbData()

    getHTML.GetHTML1().saveHTML1()
