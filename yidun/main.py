import requests
import execjs
import json
import random

'''
易盾空间验证mode
'''

dt = "8KItRxeHpqNAQlUEFAPFvYHrY2faPyR2"
class YiDun(object):
    def __init__(self):
        self.session = requests.session()
        self.headers = {
            'Accept': '*/*',
            'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
            'Cache-Control': 'no-cache',
            'Connection': 'keep-alive',
            'Pragma': 'no-cache',
            'Referer': 'https://dun.163.com/',
            'Sec-Fetch-Dest': 'script',
            'Sec-Fetch-Mode': 'no-cors',
            'Sec-Fetch-Site': 'same-site',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36',
            'sec-ch-ua': '"Google Chrome";v="123", "Not:A-Brand";v="8", "Chromium";v="123"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
        }


    def download_img(self, image_url, name):
        response = requests.get(url=image_url, headers=self.headers)
        img = response.content
        path=f'./{name}.jpg'
        with open(path, 'wb') as f:
            f.write(img)
        print(f'{name}图片保存成功')

    def main(self):
        # 请求d
        url_d = 'https://ac.dun.163.com/v3/d'
        payload_d = execjs.compile(open('./yidun_d_b.js', encoding="utf-8").read()).call("get_d_d")
        data = f'd={payload_d}&v=33d41777&cb=__wmjsonp_09596e4'
        resp_d = self.session.post(url=url_d, headers=self.headers, data=data).text
        # print(resp)
        resp_d = resp_d[resp_d.index('(') + 1: resp_d.rindex(')')]
        resp_d = json.loads(resp_d)

        # 请求b
        a = resp_d[2]
        r = resp_d[3]
        url_b = 'https://ac.dun.163.com/v3/b'
        payload_d = execjs.compile(open('./yidun_d_b.js', encoding="utf-8").read()).call("get_b_d", a, r)
        data = f'd={payload_d}&v=33d41777&cb=__wmjsonp_fdb7524'
        resp_b = self.session.post(url=url_b, headers=self.headers, data=data).text
        resp_b = resp_b[resp_b.index('(') + 1: resp_b.rindex(')')]
        resp_b = json.loads(resp_b)


        # 请求get
        d = resp_d[3]
        acToken = execjs.compile(open('./yidun_d_b.js', encoding="utf-8").read()).call("get_actoken", d)
        fp = execjs.compile(open('./yidun_fp.js', encoding="utf-8").read()).call("get_fp")
        # fp = r'grYylTIdWoEW39L5\g3WBIlMvP4CBHw+mV8alNDpierz\njTrjsd6byLNpQ2q7XaRvm\h0QiKxAdRNw7EozShGmCP8zQnwKJ2o2INE3jTDCAIrvbkf2i5LI0kx7sYBt\8c6ezdR0/gkhfOy959djZ5mf\rwOllVxODoq5CSqGiH1RAxv:1711882951010'
        cb = execjs.compile(open('./yidun_data.js', encoding="utf-8").read()).call("get_cb")
        callback = execjs.compile(open('./yidun_data.js', encoding="utf-8").read()).call("get_callback")
        url_get = "https://c.dun.163.com/api/v3/get"
        params = {
            "referer": "https://dun.163.com/trial/space-inference",
            "zoneId": "CN31",
            "dt": dt,
            "acToken": acToken,
            "id": "07e2387ab53a4d6f930b8d9a9be71bdf",
            "fp": fp,
            "https": "true",
            "type": "11",
            "version": "2.26.1",
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
        resp_get = self.session.get(url=url_get, headers=self.headers, params=params).text
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

        # 最终请求
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
            "id": "07e2387ab53a4d6f930b8d9a9be71bdf",
            "token": token,
            "acToken": "undefined",
            "data": data,
            "width": "320",
            "type": "11",
            "version": "2.26.1",
            "cb": cb,
            "extraData": "",
            "bf": "0",
            "runEnv": "10",
            "sdkVersion": "undefined",
            "iv": "3",
            "callback": callback
        }
        resp_check = self.session.get(url=url_check, headers=self.headers, params=params).text
        resp_check = resp_check[resp_check.index('(') + 1: resp_check.rindex(')')]
        resp_check = json.loads(resp_check)
        print('最终结果:\n')
        print(resp_check['data']['result'])
        print(resp_check['data']['validate'])

        



yidun = YiDun()
yidun.main()
# yidun.download_img('https://necaptcha.nosdn.127.net/228dfcbbcbdd4b2f9cd800e063f0ab54.jpg', 'img2')