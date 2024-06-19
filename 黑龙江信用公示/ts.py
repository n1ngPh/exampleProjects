import rsa
import random
import io
from pathlib import Path
from PIL import Image
import json
import ddddocr
import requests
import time
import re
import execjs
def run(searchWord):
    secret_key = "e6a1059d8d5fb341"
    def rsa_encrypt(random):
        """
        rsa加密
        :param random: 随机数
        :return: 加密后的随机数
        """
        # 公钥模数
        n = '00C1E3934D1614465B33053E7F48EE4EC87B14B95EF88947713D25EECBFF7E74C7977D02DC1D9451F79DD5D1C10C29ACB6A9B4D6FB7D0A0279B6719E1772565F09AF627715919221AEF91899CAE08C0D686D748B20A3603BE2318CA6BC2B59706592A9219D0BF05C9F65023A21D2330807252AE0066D59CEEFA5F2748EA80BAB81'
        # 公钥指数
        e = '10001'
        # 构造公钥
        key = rsa.PublicKey(e=int(e, 16), n=int(n, 16))
        # print('key:',key)
        # 加密
        message = rsa.encrypt(random.encode('utf-8'), key)
        # 转换成16进制
        encrypt_data = message.hex()
        return encrypt_data

    H7z = rsa_encrypt(secret_key)

    session = requests.session()
    t = time.time()*1000
    url = "http://gsxt.hlj.gov.cn/registerValidate.jspx?{}".format(t)
    r = session.get(url=url)
    print(r.text)
    gt = r.json()['gt']

    challenge = r.json()['challenge']
    url = "http://api.geetest.com/gettype.php"
    params = {
        "gt":gt,
        "callback":"geetest_{}".format(int(time.time()*1000))
    }
    r = session.get(url=url,params=params)
    print(r.text)
    url = "http://api.geetest.com/get.php"
    params = {
        "gt":gt,
        "challenge":challenge,
        "product": "popup",
        "offline": "false",
        "protocol": "http://",
        "type": "slide",
        "path": "/static/js/geetest.6.0.9.js",
        "callback": "geetest_{}".format(int(time.time()*1000))
    }
    r = session.get(url=url,params=params)
    jsonData = re.findall("\((.*?)\)",r.text,re.S)[0]
    # print(callback)
    res = json.loads(jsonData)
    c = res['c']
    s = res['s']
    bg = res['bg']
    slice = res['slice']
    challenge = res['challenge']
    gt = res['gt']
    url = "http://static.geetest.com/"
    bg = session.get(url+bg).content
    slice = session.get(url+slice).content
    print(r.text)
    with open("./bg.webp","wb") as f:
        f.write(bg)
    with open("./slice.png","wb") as f:
        f.write(slice)
    def get_merge_image(imurl):  # 传入带缺口信息的图片的地址
        location_list = [{"x": -157, "y": -58}, {"x": -145, "y": -58}, {"x": -265, "y": -58}, {"x": -277, "y": -58},
                         {"x": -181, "y": -58}, {"x": -169, "y": -58}, {"x": -241, "y": -58}, {"x": -253, "y": -58},
                         {"x": -109, "y": -58}, {"x": -97, "y": -58}, {"x": -289, "y": -58}, {"x": -301, "y": -58},
                         {"x": -85, "y": -58}, {"x": -73, "y": -58}, {"x": -25, "y": -58}, {"x": -37, "y": -58},
                         {"x": -13, "y": -58}, {"x": -1, "y": -58}, {"x": -121, "y": -58}, {"x": -133, "y": -58},
                         {"x": -61, "y": -58}, {"x": -49, "y": -58}, {"x": -217, "y": -58}, {"x": -229, "y": -58},
                         {"x": -205, "y": -58}, {"x": -193, "y": -58}, {"x": -145, "y": 0}, {"x": -157, "y": 0},
                         {"x": -277, "y": 0}, {"x": -265, "y": 0}, {"x": -169, "y": 0}, {"x": -181, "y": 0},
                         {"x": -253, "y": 0}, {"x": -241, "y": 0}, {"x": -97, "y": 0}, {"x": -109, "y": 0},
                         {"x": -301, "y": 0}, {"x": -289, "y": 0}, {"x": -73, "y": 0}, {"x": -85, "y": 0},
                         {"x": -37, "y": 0}, {"x": -25, "y": 0}, {"x": -1, "y": 0}, {"x": -13, "y": 0},
                         {"x": -133, "y": 0}, {"x": -121, "y": 0}, {"x": -49, "y": 0}, {"x": -61, "y": 0},
                         {"x": -229, "y": 0}, {"x": -217, "y": 0}, {"x": -193, "y": 0}, {"x": -205, "y": 0}]


        im = Image.open(imurl)

        im_list_upper = []
        im_list_down = []
        for location in location_list:
            if location['y'] == -58:
                im_list_upper.append(
                    im.crop((abs(location['x']), 58, abs(location['x']) + 10, 116)))  # 有关参数的介绍请看下方的crop方法的介绍， 可自行调整
            if location['y'] == 0:
                im_list_down.append(im.crop((abs(location['x']), 0, abs(location['x']) + 10, 0 + 58)))

        new_im = Image.new('RGB', (260, 116))  # 生成的图片的大小， 可调整

        x_offset = 0
        for im in im_list_upper:
            new_im.paste(im, (x_offset, 0))
            x_offset += im.size[0]

        x_offset = 0
        for im in im_list_down:
            new_im.paste(im, (x_offset, 58))
            x_offset += im.size[0]
        new_im.save("./bg.jpg")
        # 将重组之后的图片进行返回 也可直接使用 new_im.save("./captcha.png") 保存
    get_merge_image("bg.webp")

    slide = ddddocr.DdddOcr(det=False, ocr=False)

    with open('./slice.png', 'rb') as f:
        target_bytes = f.read()
    with open('./bg.jpg', 'rb') as f:
        background_bytes = f.read()

    res = slide.slide_match(target_bytes, background_bytes)
    setLeft = int(res['target'][0])
    def get_track(distance):
        if not isinstance(distance, int) or distance < 0:
            raise ValueError(f"distance类型必须是大于等于0的整数: distance: {distance}, type: {type(distance)}")
        slide_track = [
            [random.randint(-50, -10), random.randint(-50, -10), 0],
            [0, 0, 0],
        ]
        count = 30 + int(distance / 2)
        t = random.randint(50, 100)
        _x = 0
        _y = 0
        for i in range(count):
            if (i / count) == 1:
                ease_out_expo = 1
            else:
                ease_out_expo = 1 - pow(2, -10 * (i / count))
            x = round(ease_out_expo * distance)
            t += random.randint(10, 20)
            if x == _x:
                continue
            slide_track.append([x, _y, t])
            _x = x
        slide_track.append(slide_track[-1])
        return slide_track
    track = get_track(setLeft)

    passtime = track[len(track)-1][2]       #验证时间
    print("passtime--->"+str(passtime))
    userresponse = execjs.compile(open("ts.js", encoding="utf-8").read()).call("getUserresponse", setLeft, challenge)
    print("track---->" + str(track))
    F7z = execjs.compile(open("ts.js", encoding="utf-8").read()).call("getF7z", track, c, s)  #track为轨迹,c、s为返回值。
    print("F7z------>" + F7z)
    rp = execjs.compile(open("ts.js", encoding="utf-8").read()).call("get_rp", gt, challenge, passtime) #gt和challenge为第二次返回的值
    imgload = random.randint(1,500)
    Y7z = {
        'userresponse': userresponse,
        'rp':rp,                #gt、challenge、passtime加密得到
        'passtime': passtime,   #滑块通过时间
        'imgload': imgload, #固定值
        'aa': F7z,          #轨迹加密得到
        'ep': {"v": "6.0.9"}
    }
    q7z = execjs.compile(open("ts.js", encoding="utf-8").read()).call("get_q7z", Y7z, secret_key)   #secret_key为加密得到H7z的key
    r7z = execjs.compile(open("ts.js", encoding="utf-8").read()).call("get_r7z", q7z)
    w = r7z + H7z
    params = {
        "gt":gt,
        "challenge":challenge,
        "w":w,
        "callback":"geetest_{}".format(int(time.time()*1000))
    }
    print("w----->"+w)
    r = session.get("http://api.geevisit.com/ajax.php",params=params)
    jsonData = re.findall("\((.*?)\)",r.text,re.S)[0]
    # print(callback)
    print(r.text)
    res = json.loads(jsonData)
    validate = res['validate']
    print("validate----->"+validate)

    data = {
        "searchText": searchWord,
        "geetest_challenge": challenge,
        "geetest_validate": validate,
        "geetest_seccode": "{}|jordan".format(validate)
    }
    r = session.post("http://gsxt.hlj.gov.cn/validateSecond.jspx",data=data)
    params = {
        "top": "top",
        "checkNo": validate,
        "searchType": "1",
        "entName": searchWord
    }
    r = session.get("http://gsxt.hlj.gov.cn/searchList.jspx",params=params)
    print(r.text)
if __name__ == "__main__":
    searchWord = "齐齐哈尔立泰商贸有限公司"
    run(searchWord)