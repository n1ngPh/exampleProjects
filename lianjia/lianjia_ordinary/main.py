import random
import requests
from lxml import html
import time
import pymysql

class Spider(object):
    def __init__(self):
        self.session = requests.session()
        self.num = 0
        self.conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='', db='mysql', charset='utf8')
        self.cursor = self.conn.cursor()

    def get_UA(self):
        user_agent_list = [
            "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 "
            "(KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1",
            "Mozilla/5.0 (X11; CrOS i686 2268.111.0) AppleWebKit/536.11 "
            "(KHTML, like Gecko) Chrome/20.0.1132.57 Safari/536.11",
            "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.6 "
            "(KHTML, like Gecko) Chrome/20.0.1092.0 Safari/536.6",
            "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.6 "
            "(KHTML, like Gecko) Chrome/20.0.1090.0 Safari/536.6",
            "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.1 "
            "(KHTML, like Gecko) Chrome/19.77.34.5 Safari/537.1",
            "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/536.5 "
            "(KHTML, like Gecko) Chrome/19.0.1084.9 Safari/536.5",
            "Mozilla/5.0 (Windows NT 6.0) AppleWebKit/536.5 "
            "(KHTML, like Gecko) Chrome/19.0.1084.36 Safari/536.5",
            "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 "
            "(KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
            "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/536.3 "
            "(KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_0) AppleWebKit/536.3 "
            "(KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
            "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 "
            "(KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3",
            "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 "
            "(KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3",
            "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 "
            "(KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
            "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 "
            "(KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
            "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/536.3 "
            "(KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
            "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 "
            "(KHTML, like Gecko) Chrome/19.0.1061.0 Safari/536.3",
            "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/535.24 "
            "(KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24",
            "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/535.24 "
            "(KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24",
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
            "(KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36 Edg/113.0.1774.50"
        ]
        return random.choice(user_agent_list)

    def get_resp(self, url):
        headers = {'user-agent': self.get_UA()}
        resp = self.session.get(url=url, headers=headers)
        return resp

    def extract_data(self, resp):
        house_list = html.etree.HTML(resp.text).xpath('//div[@class="content__list"]/div')
        for house in house_list:
            self.item = {}
            self.item['title'] = house.xpath('./a[@class="content__list--item--aside"]/@title')[0]
            self.item['link'] = 'https://nj.lianjia.com' + house.xpath(
                './a[@class="content__list--item--aside"]/@href')[0]
            self.item['location'] = '.'.join(house.xpath('./div/p[2]/a/text()'))
            self.detail_data(self.item['link'])
            self.save_data()
            self.num += 1
    def detail_data(self, url):
        resp = self.get_resp(url)
        data = html.etree.HTML(resp.text)
        try:
            # 租金
            self.item['rent'] = data.xpath('//*[@id="aside"]/div[1]/span/text()')[0]
        except:
            self.item['rent'] = 'None'
        try:
            # 类型
            self.item['apartment_type'] = data.xpath('//*[@id="aside"]/ul/li[1]/text()')[0]
        except:
            self.item['apartment_type'] = 'None'

        try:
            # 公寓布局
            self.item['apartment_layout'] = data.xpath('//*[@id="aside"]/ul/li[2]/text()')[0]
        except:
            self.item['apartment_layout'] = 'None'

        try:
            # 方向
            self.item['orientation'] = data.xpath('//*[@id="aside"]/ul/li[3]/span[2]/text()')[0]
        except:
            self.item['orientation'] = 'None'

        try:
            # 发布时间
            self.item['publish_time'] = data.xpath('//html/body/div[3]/div[1]/div[3]/div[1]/text()')[0].replace(
                '房源维护时间：', '').strip()
        except:
            self.item['publish_time'] = 'None'

        try:
            # 楼层
            self.item['floor'] = data.xpath('//*[@id="info"]/ul[1]/li[8]/text()')[0].replace('楼层：', '')
        except:
            self.item['floor'] = 'None'

    def save_data(self):
        insert_sql = """insert into lianjia1(title, link, location, rent, apartment_type, apartment_layout, orientation, publish_time, floor)
                                Values(%s, %s, %s, %s, %s, %s, %s, %s, %s);"""
        self.cursor.execute(insert_sql, (self.item['title'], self.item['link'], self.item['location'], self.item['rent'], self.item['apartment_type'],
                                    self.item['apartment_layout'], self.item['orientation'], self.item['publish_time'], self.item['floor']))
        self.conn.commit()
        print(self.item)

    def read_urls(self):
        with open(r"D:\CodeProjects\PycharmProjects\CrawlerProject-master\lianjia_scrapy\url_list.txt", 'r') as f:
            urls = [url.strip() for url in f.readlines()]
        return urls

    def main(self):
        url_list = self.read_urls()
        for url in url_list:
            resp = self.get_resp(url)
            self.extract_data(resp)

        self.cursor.close()
        print(f'总房源数：{self.num}')

if __name__ == '__main__':
    start = time.time()
    spider = Spider()
    spider.main()
    end = time.time()
    print(f'总耗时{end-start}')