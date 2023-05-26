# -*- coding: UTF-8 -*-
'''
@Project ：learning 
@File    ：验证码1.py
@IDE     ：PyCharm 
@Author  ：ning
@Date    ：2023/5/14 19:09 
'''

from loguru import logger
import re
import execjs
import requests
import cv2


class Verification(object):
    def __init__(self):
        self.session = requests.session()

        self.path_puzzleImg = 'img/puzzleImg.png'
        self.path_baImg = 'img/bgimg.png'
        self.path_out = 'img/myimg.png'

        self.ctx = execjs.compile(open('验证码1.js', encoding='utf-8').read())

    def get_sessionId(self):
        url = 'https://www.anjuke.com/captcha-verify/?callback=shield&from=antispam'
        resp = self.session.get(url=url)
        self.sessionId = re.findall("'sessionId' : '(.*?)',", resp.text)[0]
        logger.info(f"sessionId ==> {self.sessionId}")

    def get_dInfo(self):
        _cRV = {
            "sdkv": "3.0.1",
            "busurl": "https://www.anjuke.com/captcha-verify/?callback=shield&from=antispam",
            "useragent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36 Edg/113.0.1774.42",
            "clienttype": "1"
        }
        _2undefinedp = self.sessionId
        self.dInfo = self.ctx.call('AESencrypt', _cRV, _2undefinedp)
        logger.info(f"dInfo ==> {self.dInfo}")

    def req_getinfotp(self):
        url = 'https://verifycode.58.com/captcha/getInfoTp'
        args = f'sessionId={self.sessionId}&showType=embed&track=&clientType=1&clientId=1&language=zh-CN&' \
               f'dInfo={self.dInfo}'

        resp = self.session.post(url=url, data=args).json()
        self.info = resp['data']['info']
        self.responseId = resp['data']['responseId']
        logger.info(f"info ==> {self.info}")
        logger.info(f"responseId ==> {self.responseId}")

    def down_img(self):
        img_info = self.ctx.call('AESdecrypt', self.info, self.sessionId)

        # bg: 背景图片
        bgImgUrl = img_info['bgImgUrl']
        resp_bgImg = self.session.get(url=bgImgUrl)
        with open(self.path_baImg, 'wb') as f:
            f.write(resp_bgImg.content)
        # 缺口图片
        puzzleImgUrl = img_info['puzzleImgUrl']
        resp_puzzleImg = self.session.get(url=puzzleImgUrl)
        with open(self.path_puzzleImg, 'wb') as f:
            f.write(resp_puzzleImg.content)

    def identify_gap(self):
        # 读取背景图片和缺口图片
        bg_img = cv2.imread(self.path_baImg)  # 背景图片
        tp_img = cv2.imread(self.path_puzzleImg)  # 缺口图片

        # 识别图片边缘
        bg_edge = cv2.Canny(bg_img, 100, 200)
        tp_edge = cv2.Canny(tp_img, 100, 200)

        # 转换图片格式
        bg_pic = cv2.cvtColor(bg_edge, cv2.COLOR_GRAY2RGB)
        tp_pic = cv2.cvtColor(tp_edge, cv2.COLOR_GRAY2RGB)

        # 缺口匹配
        res = cv2.matchTemplate(bg_pic, tp_pic, cv2.TM_CCOEFF_NORMED)
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)  # 寻找最优匹配

        # 绘制方框
        th, tw = tp_pic.shape[:2]
        tl = max_loc  # 左上角点的坐标
        br = (tl[0] + tw, tl[1] + th)  # 右下角点的坐标
        cv2.rectangle(bg_img, tl, br, (0, 0, 255), 2)  # 绘制矩形
        cv2.imwrite(self.path_out, bg_img)  # 保存在本地

        self.distance = int(tl[0] * 0.583333)
        logger.info(f"缺口位置==> {tl[0]}")
        logger.info(f"缩放后==> {self.distance}")

    def generate_track(self):
        ratio = self.distance/180
        new_track = ""
        base_track = "33,23,0|34,23,91|35,23,96|36,23,100|37,23,104|38,23,106|39,23,109|40,23,113|41,23,116|42,23,118|43,23,121|44,23,124|45,23,126|46,23,128|47,23,131|48,23,133|49,23,136|50,23,138|51,23,139|52,23,141|54,23,143|55,23,146|56,23,147|57,23,148|58,23,150|59,23,151|60,23,152|61,22,154|62,22,156|63,22,157|64,22,158|65,22,160|66,22,161|68,22,163|69,22,165|70,22,166|71,22,167|72,22,170|73,22,171|74,22,171|75,22,173|76,22,174|77,22,176|78,22,177|79,22,178|81,22,180|82,22,182|83,22,183|85,22,185|86,22,186|87,22,187|88,22,189|89,22,190|90,22,191|91,22,192|92,22,194|94,22,195|95,22,197|96,22,198|97,22,199|98,22,200|100,22,202|101,22,204|103,22,206|104,22,208|105,22,209|106,22,211|107,22,212|108,22,213|109,22,216|110,22,217|111,22,218|112,22,220|113,22,222|114,22,223|115,22,225|116,22,226|117,22,228|119,22,230|120,22,233|121,22,236|122,22,237|123,22,238|124,22,241|125,22,243|126,22,245|127,22,246|128,22,248|129,22,251|131,22,253|132,22,255|133,22,257|134,22,259|135,22,260|136,22,262|137,22,264|139,22,266|140,22,269|141,22,270|143,22,272|144,22,274|145,22,276|146,22,277|147,22,279|148,22,280|149,22,282|150,22,283|151,22,285|152,22,287|153,22,289|154,22,290|155,22,292|156,22,294|157,22,297|158,22,298|159,22,301|160,22,304|161,22,311|162,22,311|163,22,314|164,22,319|165,22,322|166,21,325|167,21,328|168,21,332|169,21,337|170,21,338|171,21,341|172,21,343|173,21,346|175,21,353|176,21,355|177,21,359|178,21,363|179,21,364|180,21,369|181,21,377|182,21,431|183,21,437|184,21,447|185,21,501|186,21,509|187,21,510|188,21,515|189,21,516|190,21,519|191,21,522|192,21,523|193,21,525|194,21,528|195,21,529|196,21,533|197,21,536|198,21,540|199,21,543|200,21,701|201,21,759|202,21,766|203,21,770|204,21,778|205,21,785|206,21,842|207,21,855|208,21,856|209,21,866|210,21,964|211,21,1763|212,21,1770|213,21,1785|213,21,2444|"
        base_track = base_track.split("|")[:-1]
        for track in base_track:
            t = track.split(",")
            new_track += str(int(int(t[0]) * ratio)) + "," + str(t[1]) + "," + str(int(int(t[2]) * ratio)) + "|"

        logger.info(f"生成轨迹 ==> {new_track}")
        logger.info(f"轨迹长度 ==> {(len(new_track))}")
        return new_track

    def req_checkInfoTp(self):
        _Ug0 = {
            'x': self.distance,
            'track': self.generate_track(),
            'p': [0, 0]
        }
        self.data = self.ctx.call('AESencrypt', _Ug0, self.sessionId)
        url = 'https://verifycode.58.com/captcha/checkInfoTp'
        args = f'sessionId={self.sessionId}&' \
               f'responseId={self.responseId}&' \
               f'dInfo={self.dInfo}&' \
               'language=zh-CN&' \
               f'data={self.data}'
        resp = self.session.post(url=url, data=args).json()
        logger.success(resp['message'])

    def main(self):
        self.get_sessionId()
        self.get_dInfo()
        # 请求响应得到info、responseId,然后解密生成验证码图片URL
        self.req_getinfotp()
        # 保存验证码图片到本地
        self.down_img()
        # 获取缺口X位置
        self.identify_gap()
        # 最终校验
        self.req_checkInfoTp()


if __name__ == '__main__':
    verification = Verification()
    verification.main()