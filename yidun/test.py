import time
import math
import requests
import execjs
import json
import re
import trace
import ddddocr
import random


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
        self.tracks_list = [
            [[4, -1, 441], [5, -1, 444], [6, -1, 449], [7, -1, 450], [8, -1, 454], [9, -1, 457], [10, -1, 461], [11, -1, 464], [12, -1, 469], [12, 0, 512], [13, 0, 550], [14, 0, 559], [15, 1, 564], [16, 1, 567], [17, 1, 570], [18, 1, 576], [19, 1, 580], [20, 2, 582], [21, 2, 587], [22, 2, 594], [23, 2, 660], [24, 2, 665], [25, 2, 671], [26, 2, 675], [27, 3, 679], [28, 3, 680], [29, 3, 684], [30, 3, 685], [31, 3, 688], [32, 3, 690], [33, 3, 691], [34, 3, 694], [34, 4, 696], [35, 4, 696], [36, 4, 697], [37, 4, 700], [38, 4, 702], [38, 5, 704], [39, 5, 705], [40, 5, 707], [41, 5, 709], [42, 5, 714], [43, 5, 718], [44, 5, 721], [45, 5, 724], [45, 6, 726], [46, 6, 727], [47, 6, 734], [48, 6, 738], [49, 6, 742], [50, 6, 747], [51, 6, 750], [52, 6, 754], [53, 6, 757], [54, 6, 760], [55, 6, 765], [55, 7, 766], [56, 7, 769], [57, 7, 771], [58, 7, 775], [59, 7, 779], [60, 7, 781], [61, 7, 783], [62, 7, 787], [63, 7, 790], [64, 7, 793], [65, 7, 793], [66, 7, 797], [67, 7, 799], [68, 7, 802], [69, 7, 803], [69, 8, 805], [70, 8, 806], [71, 8, 808], [72, 8, 809], [73, 8, 810], [74, 8, 813], [75, 8, 815], [76, 8, 818], [77, 8, 821], [78, 9, 822], [79, 9, 825], [80, 9, 827], [81, 9, 830], [82, 9, 831], [83, 9, 836], [84, 9, 840], [85, 9, 889], [86, 9, 893], [87, 9, 899], [88, 9, 902], [89, 9, 904], [90, 9, 905], [91, 9, 907], [92, 10, 910], [93, 10, 912], [94, 10, 913], [95, 10, 915], [96, 10, 917], [97, 10, 919], [98, 10, 920], [99, 10, 922], [100, 10, 924], [101, 10, 926], [102, 10, 927], [103, 10, 930], [104, 10, 931], [105, 10, 933], [106, 10, 935], [107, 10, 938], [108, 10, 942], [109, 10, 948], [110, 10, 953], [111, 10, 985], [112, 10, 990], [113, 10, 993], [114, 10, 995], [114, 11, 997], [115, 11, 997], [116, 11, 1001], [118, 11, 1004], [119, 11, 1007], [120, 11, 1010], [121, 11, 1012], [122, 11, 1013], [123, 11, 1016], [124, 11, 1018], [125, 11, 1021], [126, 11, 1023], [127, 11, 1025], [128, 11, 1028], [129, 11, 1032], [130, 11, 1034], [131, 11, 1037], [132, 11, 1042], [132, 12, 1044], [133, 12, 1045], [134, 12, 1047], [135, 12, 1051], [136, 12, 1055], [137, 12, 1057], [138, 12, 1059], [139, 12, 1061], [140, 12, 1064], [141, 12, 1067], [142, 12, 1069], [143, 13, 1071], [144, 13, 1074], [145, 13, 1077], [146, 13, 1078], [147, 13, 1081], [148, 13, 1086], [149, 13, 1137], [150, 13, 1142], [151, 13, 1147], [152, 13, 1152], [153, 13, 1154], [154, 13, 1156], [155, 13, 1159], [156, 13, 1160], [156, 14, 1161], [157, 14, 1163], [158, 14, 1166], [159, 14, 1167], [160, 14, 1170], [161, 14, 1173], [162, 14, 1177], [163, 14, 1178], [164, 14, 1183], [165, 14, 1237], [166, 14, 1248], [166, 15, 1251], [167, 15, 1253], [168, 15, 1308], [169, 15, 1316], [170, 15, 1321], [171, 15, 1324], [172, 15, 1328], [173, 15, 1332], [174, 15, 1335], [175, 15, 1337], [176, 15, 1340], [177, 15, 1344], [178, 15, 1349], [179, 15, 1417], [180, 15, 1530], [180, 16, 1609], [181, 16, 1619], [182, 16, 1665], [183, 16, 1670], [184, 16, 1683], [185, 16, 1934], [186, 16, 1941], [187, 16, 1944], [188, 16, 1950], [189, 16, 2032]],
            [[4, 0, 112], [5, 0, 116], [6, 0, 119], [7, 0, 121], [8, 0, 126], [9, 0, 128], [10, 0, 131], [11, 0, 132], [12, 0, 135], [13, 0, 138], [14, 0, 141], [15, 0, 143], [16, 0, 145], [17, 0, 148], [18, 0, 151], [19, 0, 152], [20, 0, 155], [21, 0, 158], [22, 0, 161], [23, 0, 163], [24, 0, 166], [25, 0, 170], [26, 0, 174], [27, 0, 179], [28, 0, 181], [29, 0, 186], [30, 0, 192], [31, 0, 198], [32, 0, 202], [33, 0, 206], [34, 0, 211], [35, 0, 213], [36, 0, 215], [37, 0, 217], [38, 0, 220], [39, 0, 223], [40, 0, 224], [41, 0, 226], [42, 0, 228], [43, 0, 229], [44, 0, 230], [46, 0, 231], [47, 0, 233], [48, 0, 234], [50, 0, 236], [51, 1, 237], [52, 1, 238], [53, 1, 239], [54, 1, 240], [55, 1, 241], [57, 1, 242], [58, 1, 243], [60, 1, 244], [61, 1, 246], [63, 1, 248], [65, 1, 249], [67, 1, 251], [71, 2, 253], [74, 2, 255], [75, 2, 257], [77, 2, 258], [79, 2, 261], [81, 2, 262], [83, 2, 264], [85, 2, 266], [86, 2, 268], [88, 2, 270], [89, 2, 271], [90, 2, 272], [92, 2, 275], [93, 2, 276], [94, 2, 278], [95, 2, 280], [96, 2, 283], [97, 2, 287], [98, 2, 323], [99, 2, 327], [100, 2, 333], [101, 2, 338], [102, 2, 341], [103, 2, 344], [104, 2, 347], [105, 2, 350], [106, 3, 354], [107, 3, 355], [108, 3, 357], [109, 3, 359], [110, 3, 362], [111, 3, 364], [112, 3, 366], [113, 3, 369], [114, 3, 373], [115, 3, 379], [116, 3, 411], [117, 3, 419], [118, 3, 422], [119, 3, 425], [120, 3, 426], [121, 3, 428], [122, 3, 430], [123, 3, 432], [124, 3, 433], [125, 3, 434], [126, 3, 436], [127, 3, 437], [128, 3, 438], [129, 3, 440], [130, 3, 441], [131, 3, 442], [132, 3, 443], [133, 3, 444], [134, 3, 445], [135, 3, 447], [137, 3, 448], [138, 3, 450], [139, 3, 451], [140, 3, 452], [141, 3, 453], [142, 3, 454], [143, 3, 455], [145, 3, 456], [146, 3, 458], [147, 3, 459], [148, 3, 460], [149, 3, 461], [150, 3, 462], [152, 3, 464], [153, 3, 466], [155, 3, 468], [155, 2, 469], [156, 2, 470], [157, 2, 472], [158, 2, 475], [159, 2, 476], [160, 2, 480], [161, 2, 485], [162, 2, 536], [163, 2, 538], [164, 2, 542], [165, 2, 545], [166, 2, 547], [167, 2, 548], [168, 2, 551], [169, 2, 553], [170, 2, 555], [171, 2, 558], [172, 2, 559], [173, 2, 560], [174, 2, 563], [175, 2, 565], [176, 2, 566], [177, 2, 568], [178, 2, 571], [179, 2, 573], [180, 2, 575], [181, 2, 579], [182, 2, 583], [183, 2, 623], [184, 2, 630], [185, 2, 635], [186, 2, 637], [187, 2, 640], [188, 2, 641], [189, 2, 645], [190, 2, 648], [191, 2, 650], [192, 2, 651], [193, 2, 653], [193, 3, 654], [194, 3, 654], [196, 3, 657], [197, 3, 658], [198, 3, 661], [199, 3, 662], [200, 3, 665], [201, 3, 667], [202, 3, 671], [203, 3, 673], [204, 3, 676], [205, 3, 728], [206, 3, 736], [207, 3, 746], [208, 3, 749], [209, 3, 888], [210, 3, 905], [211, 3, 918], [212, 3, 923], [213, 3, 979], [214, 3, 1003], [215, 3, 1008], [216, 3, 1011], [217, 3, 1014], [218, 3, 1018], [219, 3, 1022], [220, 3, 1024], [221, 3, 1031], [222, 3, 1196], [222, 2, 1198], [223, 2, 1272], [224, 2, 1280], [224, 1, 1293], [225, 1, 1300], [226, 1, 1379], [227, 1, 1399], [227, 0, 1408], [228, 0, 1484], [229, 0, 1712], [229, 0, 1979], [229, -1, 2634], [229, -2, 2840], [230, -2, 3107], [231, -2, 3119], [231, -3, 3126], [232, -3, 3542], [233, -3, 3547], [233, -4, 3556], [234, -4, 3558], [233, -4, 4269], [233, -5, 4358], [233, -6, 4600]],
        ]
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36",
        }

    def imitate_track(self, distance):
        tracks = random.choice(self.tracks_list)
        old_distance = int(tracks[-1][0])
        scale = distance / old_distance
        new_track = []
        for track in tracks:
            new_x = 4 if int(track[0]*scale) < 4 else math.ceil(track[0]*scale)
            new_time = int(track[2]*scale)
            atom = [new_x, track[1], new_time]
            new_track.append(atom)
        return new_track

    def download_img(self, image_url, name):
        if image_url:
            response = requests.get(url=image_url)
            img = response.content
            path = f'./{name}.jpg'
            with open(path, 'wb') as f:
                f.write(img)
            print(f'{name}图片保存成功')

    def get_distance(self, bg_url, front_url):
        slide = ddddocr.DdddOcr(det=False, ocr=False)
        background_bytes = requests.get(bg_url, headers=self.headers).content
        path = f'./bg.jpg'
        with open(path, 'wb') as f:
            f.write(background_bytes)
        print(f'bg_url图片保存成功')

        target_bytes = requests.get(front_url, headers=self.headers).content
        path = f'./front.jpg'
        with open(path, 'wb') as f:
            f.write(target_bytes)
        print(f'front图片保存成功')

        res = slide.slide_match(target_bytes, background_bytes, simple_target=True)
        slider_distance = res.get("target")[0]
        # 这里需要在识别出来的距离上+10，应该是跟图片大小有关导致的，需要自己去进行调整
        slider_distance = slider_distance + 5
        return slider_distance

    def main(self):

        # 获得配置信息
        url_getconf = "https://c.dun.163.com/api/v2/getconf"
        id = '07e2387ab53a4d6f930b8d9a9be71bdf'
        callback = execjs.compile(self.data_code).call("get_callback")
        params = {
            "referer": "https://dun.163.com/trial/jigsaw",
            "zoneId": "",
            "id": id,
            "ipv6": "false",
            "runEnv": "10",
            "iv": "4",
            "type": "2",
            "loadVersion": "2.4.0",
            "callback": callback
        }
        headers = {
            "Accept": "*/*",
            "Accept-Encoding": "gzip, deflate, br, zstd",
            "Accept-Language": "zh-CN,zh;q=0.9",
            "Cache-Control": "no-cache",
            "Connection": "keep-alive",
            "Host": "c.dun.163.com",
            "Pragma": "no-cache",
            "Referer": "https://dun.163.com/",
            "Sec-Fetch-Dest": "script",
            "Sec-Fetch-Mode": "no-cors",
            "Sec-Fetch-Site": "same-site",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36",
            "sec-ch-ua": "\"Chromium\";v=\"122\", \"Not(A:Brand\";v=\"24\", \"Google Chrome\";v=\"122\"",
            "sec-ch-ua-mobile": "?0"
        }
        response = self.session.get(url=url_getconf, params=params, headers=headers)
        token = re.findall(r'"token":"(.*?)"', response.text)[0]
        dt = re.findall(r'"dt":"(.*?)"', response.text)[0]
        V = re.findall(r'"resources":\["/(.*?)/core', response.text)[0]
        time.sleep(random.uniform(1, 2))


        # 请求d
        url_d = 'https://ac.dun.163.com/v3/d'
        payload_d = execjs.compile(open('./yidun_d_b.js', encoding="utf-8").read()).call("get_d_d")
        data = f'd={payload_d}&v=33d41777&cb=__wmjsonp_7257cf3'
        headers = {
            "Accept": "*/*",
            "Accept-Encoding": "gzip, deflate, br, zstd",
            "Accept-Language": "zh-CN,zh;q=0.9",
            "Cache-Control": "no-cache",
            "Connection": "keep-alive",
            "Content-Length": "1036",
            "Content-type": "application/x-www-form-urlencoded",
            "Host": "ac.dun.163.com",
            "Origin": "https://dun.163.com",
            "Pragma": "no-cache",
            "Referer": "https://dun.163.com/",
            "Sec-Fetch-Dest": "empty",
            "Sec-Fetch-Mode": "cors",
            "Sec-Fetch-Site": "same-site",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36",
            "sec-ch-ua": "\"Chromium\";v=\"122\", \"Not(A:Brand\";v=\"24\", \"Google Chrome\";v=\"122\"",
            "sec-ch-ua-mobile": "?0"
        }
        resp_d = self.session.post(url=url_d, headers=headers, data=data).text
        # print(resp)
        resp_d = resp_d[resp_d.index('(') + 1: resp_d.rindex(')')]
        resp_d = json.loads(resp_d)

        # 请求b
        a = resp_d[2]
        r = resp_d[3]
        url_b = 'https://ac.dun.163.com/v3/b'
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
        url_get = "https://c.dun.163.com/api/v3/get"
        params = {
            "referer": "https://dun.163.com/trial/jigsaw",
            "zoneId": "CN31",
            "acToken": acToken,
            "id": id,
            "fp": fp,
            "https": "true",
            "type": "2",
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
            "iv": "4",
            "width": "320",
            "audio": "false",
            "sizeType": "10",
            "smsVersion": "v3",
            "token": "",
            "callback": callback
        }
        headers = {
            "Accept": "*/*",
            "Accept-Encoding": "gzip, deflate, br, zstd",
            "Accept-Language": "zh-CN,zh;q=0.9",
            "Cache-Control": "no-cache",
            "Connection": "keep-alive",
            "Host": "c.dun.163.com",
            "Pragma": "no-cache",
            "Referer": "https://dun.163.com/",
            "Sec-Fetch-Dest": "script",
            "Sec-Fetch-Mode": "no-cors",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36",
            "Sec-Fetch-Site": "same-site"
        }
        resp_get = self.session.get(url=url_get, headers=headers, params=params).text
        resp_get = resp_get[resp_get.index('(') + 1: resp_get.rindex(')')]
        resp_get = json.loads(resp_get)
        time.sleep(random.uniform(1, 2))

        # 图片
        img1 = resp_get.get('data', {}).get('bg', [''])[0]
        # 滑块
        img2 = resp_get.get('data', {}).get('front', [''])[0]
        token = resp_get['data']['token']
        type = int(resp_get['data']['type'])



        if type == 2:
            distance = self.get_distance(img1, img2)
            print('缺口坐标距离', distance)
            # distance = int(input('请输入缺口坐标距离:'))
            # res = trace.get_track(distance)
            slider_track = self.imitate_track(distance+6)
            print(slider_track)
            data = execjs.compile(self.data_code).call('get_data_hdyz', token, distance-5.5, slider_track)
        else:
            self.download_img(img1, 'img1')
            self.download_img(img2, 'img2')
            left = int(input('请输入left坐标:'))
            top = int(input('请输入top坐标:'))
            coor = {
                'left': left,
                'top': top
            }
            # validate
            data = execjs.compile(self.data_code).call("get_data", token, coor)
            print('data:\n' + data)

        cb = execjs.compile(self.data_code).call("get_cb")
        # print('cb:\n' + cb)
        callback = execjs.compile(self.data_code).call("get_callback")
        url_check = "https://c.dun.163.com/api/v3/check"
        params = {
            "referer": "https://dun.163.com/trial/jigsaw",
            "zoneId": "CN31",
            "dt": dt,
            "id": id,
            "token": token,
            "acToken": "undefined",
            "data": data,
            "width": "320",
            "type": '2',
            "version": V,
            "cb": cb,
            "extraData": "",
            "bf": "0",
            "runEnv": "10",
            "sdkVersion": "undefined",
            "iv": "4",
            "callback": callback
        }
        headers = {
            "Accept": "*/*",
            "Accept-Encoding": "gzip, deflate, br, zstd",
            "Accept-Language": "zh-CN,zh;q=0.9",
            "Cache-Control": "no-cache",
            "Connection": "keep-alive",
            "Host": "c.dun.163.com",
            "Pragma": "no-cache",
            "Referer": "https://dun.163.com/",
            "Sec-Fetch-Dest": "script",
            "Sec-Fetch-Mode": "no-cors",
            "Sec-Fetch-Site": "same-site",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36",
            "sec-ch-ua": "\"Chromium\";v=\"122\", \"Not(A:Brand\";v=\"24\", \"Google Chrome\";v=\"122\"",
            "sec-ch-ua-mobile": "?0",
            "sec-ch-ua-platform": "\"Windows\""
        }
        resp_check = self.session.get(url=url_check, headers=headers, params=params).text
        resp_check = resp_check[resp_check.index('(') + 1: resp_check.rindex(')')]
        resp_check = json.loads(resp_check)
        result = resp_check['data']['result']
        validate = resp_check['data']['validate']
        print('最终结果:\n')
        print('validate:', result)
        print('validate:', validate)


yidun = YiDun()
for i in range(10):
    yidun.main()
# yidun.download_img('https://necaptcha.nosdn.127.net/228dfcbbcbdd4b2f9cd800e063f0ab54.jpg', 'img2')