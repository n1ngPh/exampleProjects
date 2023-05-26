# -*- coding: utf-8 -*-
import time

import scrapy
from lianjiaSpider.items import LianjiaspiderItem
import re


class LianjiazufangSpider(scrapy.Spider):
    name = 'lianjiazufang'
    allowed_domains = ['lianjia.com']
    start_urls = []
    with open(r"D:\CodeProjects\PycharmProjects\CrawlerProject-master\lianjia_scrapy\url_list.txt", 'r') as f:
        start_urls = [url.strip() for url in f.readlines()]

    def parse(self, response):
        house_list = response.xpath('//div[@class="content__list"]/div')
        for house in house_list:
            item = LianjiaspiderItem()
            item['title'] = house.xpath('./a[@class="content__list--item--aside"]/@title').extract_first()
            item['link'] = 'https://nj.lianjia.com' + house.xpath('./a[@class="content__list--item--aside"]/@href').extract_first()
            item['location'] = '.'.join(house.xpath('./div/p[2]/a/text()').extract())
            # 使用了meta = {'item': item}，将item对象作为元数据传递给了新的请求
            yield scrapy.Request(
                item['link'],
                callback=self.parse_detail,
                meta={'item': item}
            )

    def parse_detail(self, response):
        item = response.meta['item']
        print("gogogo", item)
        # 租金
        item['rent'] = response.xpath('//*[@id="aside"]/div[1]/span/text()').extract_first("none")
        # 类型
        item['apartment_type'] = response.xpath('//*[@id="aside"]/ul/li[1]/text()').extract_first("none")
        # 公寓布局
        item['apartment_layout'] = response.xpath('//*[@id="aside"]/ul/li[2]/text()').extract_first("none")
        # print(item['apartment_layout'])
        # 方向
        item['orientation'] = response.xpath('//*[@id="aside"]/ul/li[3]/span[2]/text()').extract_first("none")
        # 发布时间
        item['publish_time'] = response.xpath('//html/body/div[3]/div[1]/div[3]/div[1]/text()').extract_first("none").replace('房源维护时间：', '')
        # 楼层
        item['floor'] = response.xpath('//*[@id="info"]/ul[1]/li[8]/text()').extract_first("none").replace('楼层：', '')

        yield item
