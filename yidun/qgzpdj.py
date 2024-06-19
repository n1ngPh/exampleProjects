import requests
import execjs
import json
import re

"""
全国作品登记信息公示查询
易盾空间验证
"""


class YiDun(object):
    def __init__(self):
        self.session = requests.session()
        with open('./yidun_data.js', 'r', encoding='utf-8') as f:
            self.data_code = f.read()
        with open('./yidun_d_b.js', 'r', encoding='utf-8') as f:
            self.d_b_code = f.read()
        with open('./yidun_fp.js', 'r', encoding='utf-8') as f:
            self.fp_code = f.read()
        with open('./qgzpdj.js', 'r', encoding='utf-8') as f:
            self.qgzpdj_code = f.read()


    def download_img(self, image_url, name):
        response = requests.get(url=image_url)
        img = response.content
        path = f'./{name}.jpg'
        with open(path, 'wb') as f:
            f.write(img)
        print(f'{name}图片保存成功')

    def main(self):

        # 获得配置信息
        url_getconf = "http://c.dun.163.com/api/v2/getconf"
        callback = execjs.compile(self.data_code).call('get_callback')
        id = '159f197467664b25a1895377e53ce29e'
        params = {
            "referer": "http://qgzpdj.ccopyright.com.cn/registrationPublicity.html",
            "zoneId": "",
            "id": id,
            "ipv6": "false",
            "runEnv": "10",
            "loadVersion": "2.2.1",
            "callback": callback
        }
        headers = {
            "Accept": "*/*",
            "Accept-Encoding": "gzip, deflate",
            "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
            "Cache-Control": "no-cache",
            "Host": "c.dun.163.com",
            "Pragma": "no-cache",
            "Proxy-Connection": "keep-alive",
            "Referer": "http://qgzpdj.ccopyright.com.cn/"
        }
        response = self.session.get(url=url_getconf, params=params, headers=headers)
        token = re.findall(r'"token":"(.*?)"', response.text)[0]
        dt = re.findall(r'"dt":"(.*?)"', response.text)[0]
        V = re.findall(r'"resources":\["/(.*?)/core', response.text)[0]


        # 请求d
        url_d = 'http://ac.dun.163.com/v3/d'
        payload_d = execjs.compile(open('./yidun_d_b.js', encoding="utf-8").read()).call("get_d_d")
        data = f'd={payload_d}&v=33d41777&cb=__wmjsonp_fd09734'
        headers = {
            "Accept": "*/*",
            "Accept-Encoding": "gzip, deflate",
            "Accept-Language": "zh-CN,zh;q=0.9",
            "Cache-Control": "no-cache",
            "Connection": "keep-alive",
            "Content-Length": "1036",
            "Content-type": "application/x-www-form-urlencoded",
            "Host": "ac.dun.163.com",
            "Origin": "http://qgzpdj.ccopyright.com.cn",
            "Pragma": "no-cache",
            "Referer": "http://qgzpdj.ccopyright.com.cn/",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36"
        }
        resp_d = self.session.post(url=url_d, headers=headers, data=data).text
        # print(resp)
        resp_d = resp_d[resp_d.index('(') + 1: resp_d.rindex(')')]
        resp_d = json.loads(resp_d)

        # 请求b
        a = resp_d[2]
        r = resp_d[3]
        url_b = 'http://ac.dun.163.com/v3/b'
        payload_d = execjs.compile(self.d_b_code).call("get_b_d", a, r)
        data = f'd={payload_d}&v=33d41777&cb=__wmjsonp_e3ac57c'
        resp_b = self.session.post(url=url_b, headers=headers, data=data).text
        resp_b = resp_b[resp_b.index('(') + 1: resp_b.rindex(')')]
        resp_b = json.loads(resp_b)

        # 请求get
        d = resp_d[3]
        acToken = execjs.compile(self.d_b_code).call("get_actoken", d)
        fp = execjs.compile(self.fp_code).call("get_fp")
        # fp = r'grYylTIdWoEW39L5\g3WBIlMvP4CBHw+mV8alNDpierz\njTrjsd6byLNpQ2q7XaRvm\h0QiKxAdRNw7EozShGmCP8zQnwKJ2o2INE3jTDCAIrvbkf2i5LI0kx7sYBt\8c6ezdR0/gkhfOy959djZ5mf\rwOllVxODoq5CSqGiH1RAxv:1711882951010'
        cb = execjs.compile(self.data_code).call("get_cb")
        callback = execjs.compile(self.data_code).call("get_callback")
        url_get = "http://c.dun.163.com/api/v3/get"
        params = {
            "referer": "http://qgzpdj.ccopyright.com.cn/registrationPublicity.html",
            "zoneId": "CN31",
            "acToken": acToken,
            "id": id,
            "fp": fp,
            "https": "false",
            "type": "undefined",
            "version": V,
            "dpr": "1",
            "dev": "1",
            "cb": cb,
            "ipv6": "false",
            "runEnv": "10",
            "group": "",
            "scene": "",
            "lang": "zh-CN",
            "sdkVersion": "undefined",
            "iv": "3",
            "width": "320",
            "audio": "false",
            "sizeType": "10",
            "smsVersion": "v3",
            "token": "",
            "callback": callback
        }
        headers = {
            "Accept": "*/*",
            "Accept-Encoding": "gzip, deflate",
            "Accept-Language": "zh-CN,zh;q=0.9",
            "Cache-Control": "no-cache",
            "Connection": "keep-alive",
            "Host": "c.dun.163.com",
            "Pragma": "no-cache",
            "Referer": "http://qgzpdj.ccopyright.com.cn/",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36"
        }
        resp_get = self.session.get(url=url_get, headers=headers, params=params).text
        resp_get = resp_get[resp_get.index('(') + 1: resp_get.rindex(')')]
        resp_get = json.loads(resp_get)
        img1 = resp_get['data']['bg'][0]
        # img2 = resp_get['data']['bg'][1]
        token = resp_get['data']['token']
        print(resp_get['data']['front'])

        # 下载图片，获取坐标
        self.download_img(img1, 'img1')
        # self.download_img(img2, 'img2')
        left = int(input('请输入left坐标:'))
        top = int(input('请输入top坐标:'))
        coor = {
            'left': left,
            'top': top
        }

        # validate
        data = execjs.compile(open('./yidun_data.js', encoding="utf-8").read()).call("get_data", token, coor)
        print('data:\n' + data)
        cb = execjs.compile(open('./yidun_data.js', encoding="utf-8").read()).call("get_cb")
        print('cb:\n' + cb)
        callback = execjs.compile(open('./yidun_data.js', encoding="utf-8").read()).call("get_callback")
        url_check = "https://c.dun.163.com/api/v3/check"
        params = {
            "referer": "https://dun.163.com/trial/space-inference",
            "zoneId": "CN31",
            "dt": dt,
            "id": id,
            "token": token,
            "acToken": "undefined",
            "data": data,
            "width": "320",
            "type": "11",
            "version": V,
            "cb": cb,
            "extraData": "",
            "bf": "0",
            "runEnv": "10",
            "sdkVersion": "undefined",
            "iv": "3",
            "callback": callback
        }
        headers = {
            "Accept": "*/*",
            "Accept-Encoding": "gzip, deflate",
            "Accept-Language": "zh-CN,zh;q=0.9",
            "Cache-Control": "no-cache",
            "Connection": "keep-alive",
            "Host": "c.dun.163.com",
            "Pragma": "no-cache",
            "Referer": "http://qgzpdj.ccopyright.com.cn/",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36"
        }
        resp_check = self.session.get(url=url_check, headers=headers, params=params).text
        resp_check = resp_check[resp_check.index('(') + 1: resp_check.rindex(')')]
        resp_check = json.loads(resp_check)
        result = resp_check['data']['result']
        validate = resp_check['data']['validate']
        print('最终结果:\n')
        print('validate:', result)
        print('validate:', validate)

        # 请求recordData
        info = input('请输入要查询的内容(如: 黔作登字-2023-A-00854088):')
        gu = fp
        T1 = 'CN31'
        ticket = execjs.compile(self.qgzpdj_code).call("get_ticket", validate, gu, T1)

        parameter = {
            # "registerNumber": "国作登字-2013-M-1791",
            "registerNumber": info,
            "worksName": "",
            "owner": "",
            "ticket": ticket,
            "veriftyType": 1,
            "isOpen": 1,
            "pageIndex": 1,
            "pageSize": 10,
            "identification": "",
            "imageCode": ""
        }
        content = execjs.compile(self.qgzpdj_code).call("getStr", parameter)
        url_recordData = 'http://111.202.243.7:1317/inquire/recordData'
        data = {"registerNumber":info,
                "worksName":"","owner":"",
                "ticket":ticket,
                "veriftyType":1,"isOpen":1,"pageIndex":1,"pageSize":10,"identification":"","imageCode":"",
                "content":content}
        headers = {
            "Accept": "application/json, text/plain, */*",
            "Accept-Encoding": "gzip, deflate",
            "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
            "Cache-Control": "no-cache",
            "Content-Length": "754",
            "Content-Type": "application/json;charset=UTF-8",
            "Host": "111.202.243.7:1317",
            "Origin": "http://qgzpdj.ccopyright.com.cn",
            "Pragma": "no-cache",
            "Proxy-Connection": "keep-alive",
            "Referer": "http://qgzpdj.ccopyright.com.cn/",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36 Edg/120.0.0.0"
        }
        resp_recordData = self.session.post(url=url_recordData, headers=headers, json=data).text
        print(resp_recordData)






yidun = YiDun()
yidun.main()
# yidun.download_img('https://necaptcha.nosdn.127.net/228dfcbbcbdd4b2f9cd800e063f0ab54.jpg', 'img2')