# -*- coding: UTF-8 -*-
'''
@Project ：lianjia_ordinary 
@File    ：yibu.py
@IDE     ：PyCharm 
@Author  ：ning
@Date    ：2023/5/21 22:43 
'''

import asyncio
import aiohttp
import random
from lxml import html
import time
import pymysql


loop = asyncio.get_event_loop()

class Spider(object):
    def __init__(self):
        self.num = 0
        self.conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='', db='mysql', charset='utf8')
        self.cursor = self.conn.cursor()

        self.semaphore = asyncio.Semaphore(5)

    def get_UA(self):
        user_agent_list = [
            "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 "
            "(KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1",
            "Mozilla/5.0 (X11; CrOS i686 2268.111.0) AppleWebKit/536.11 "
            "(KHTML, like Gecko) Chrome/20.0.1132.57 Safari/536.11",
            # 省略其他User-Agent
        ]
        return random.choice(user_agent_list)

    async def get_resp(self, url):
        headers = {'user-agent': self.get_UA()}
        async with self.semaphore:
            try:
                async with self.session.get(url=url, headers=headers) as resp:
                    return await resp.text()
            except:
                print('error occurred while scraping %s', url)

    async def extract_data(self, resp):
        house_list = html.etree.HTML(resp).xpath('//div[@class="content__list"]/div')
        for house in house_list:
            self.item = {}
            self.item['title'] = house.xpath('./a[@class="content__list--item--aside"]/@title')[0]
            self.item['link'] = 'https://nj.lianjia.com' + house.xpath(
                './a[@class="content__list--item--aside"]/@href')[0]
            self.item['location'] = '.'.join(house.xpath('./div/p[2]/a/text()'))
            resp_text = await self.get_resp(self.item['link'])
            data = html.etree.HTML(resp_text)
            try:
                self.item['rent'] = data.xpath('//*[@id="aside"]/div[1]/span/text()')[0]
            except:
                self.item['rent'] = 'None'
            try:
                self.item['apartment_type'] = data.xpath('//*[@id="aside"]/ul/li[1]/text()')[0]
            except:
                self.item['apartment_type'] = 'None'
            try:
                self.item['apartment_layout'] = data.xpath('//*[@id="aside"]/ul/li[2]/text()')[0]
            except:
                self.item['apartment_layout'] = 'None'
            try:
                self.item['orientation'] = data.xpath('//*[@id="aside"]/ul/li[3]/span[2]/text()')[0]
            except:
                self.item['orientation'] = 'None'
            try:
                self.item['publish_time'] = data.xpath('//html/body/div[3]/div[1]/div[3]/div[1]/text()')[0].replace(
                    '房源维护时间：', '').strip()
            except:
                self.item['publish_time'] = 'None'
            try:
                self.item['floor'] = data.xpath('//*[@id="info"]/ul[1]/li[8]/text()')[0].replace('楼层：', '')
            except:
                self.item['floor'] = 'None'
            await self.save_data()
            self.num += 1

    async def save_data(self):
        insert_sql = """insert into lianjia2(title, link, location, rent, apartment_type, apartment_layout, orientation, publish_time, floor)
                Values(%s, %s, %s, %s, %s, %s, %s, %s, %s);"""
        self.cursor.execute(insert_sql, (self.item['title'], self.item['link'], self.item['location'], self.item['rent'], self.item['apartment_type'],
                                    self.item['apartment_layout'], self.item['orientation'], self.item['publish_time'], self.item['floor']))
        self.conn.commit()
        print(self.item)

    def read_urls(self):
        with open(r"D:\CodeProjects\PycharmProjects\CrawlerProject-master\lianjia_scrapy\url_list.txt", 'r') as f:
            urls = [url.strip() for url in f.readlines()]
        return urls

    async def main(self):
        self.session = aiohttp.ClientSession()
        url_list = self.read_urls()
        spider_resp = [asyncio.ensure_future(self.get_resp(url)) for url in url_list]
        responses = await asyncio.gather(*spider_resp)

        spider_extract = [asyncio.ensure_future(self.extract_data(resp)) for resp in responses]
        await asyncio.wait(spider_extract)

        self.cursor.close()
        await self.session.close()

if __name__ == '__main__':
    start = time.time()
    spider = Spider()

    loop.run_until_complete(spider.main())
    end = time.time()
    print(f'总耗时{end-start}')


