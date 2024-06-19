import requests
import json
import base64
import ddddocr
import execjs
import time
from urllib.parse import quote
def run(searchWord):
    headers = {
        "Accept": "*/*",
        "Accept-Encoding": "gzip, deflate",
        "Accept-Language": "zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7",
        "Cache-Control": "no-cache",
        "Connection": "keep-alive",
        "Host": 'gsxt.amr.gd.gov.cn',
        "Content-Type": "application/json",
        "Origin": "http://gsxt.amr.gd.gov.cn",
        "Referer": "http://gsxt.amr.gd.gov.cn/",
        "Pragma": "no-cache",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36",
    }

    session = requests.session()

    session.headers = headers
    r = session.get("http://gsxt.amr.gd.gov.cn/gsxt_gd/system/user/rsa/public")
    publicKey = r.json()['data']
    data = {"captchaType": "blockPuzzle","clientUid": "slider-4acef4f1-7ac7-4714-8eea-c61b36a9e0d0","ts": time.time()*1000}
    r = session.post("http://gsxt.amr.gd.gov.cn/gsxt_gd/captcha/get",data=json.dumps(data))
    jigsawImageBase64 = r.json()['repData']['jigsawImageBase64']
    originalImageBase64 = r.json()['repData']['originalImageBase64']
    token = r.json()['repData']['token']
    print("token----->"+token)
    secretKey = r.json()['repData']['secretKey']
    print("secretKey----->"+secretKey)

    image_data1 = base64.b64decode(jigsawImageBase64)
    image_data2 = base64.b64decode(originalImageBase64)
    det = ddddocr.DdddOcr(det=False, ocr=False)
    res = det.slide_match(image_data1, image_data2)

    x = 310*(res['target'][0]+10)/330
    coordinate = '{{"x":{},"y":5}}'.format(x)
    pointJson = execjs.compile(open('finalCode.js', encoding='utf-8').read()).call("encrypt", coordinate, secretKey)
    print("pointJson----->"+pointJson)
    data = {"captchaType": "blockPuzzle","pointJson": pointJson,"token": token}
    check_res = session.post("http://gsxt.amr.gd.gov.cn/gsxt_gd/captcha/check",data=json.dumps(data))
    parama1 = '%s---{"x":%s,"y":5}'%(token, x)
    captchaVerification = execjs.compile(open('finalCode.js', encoding='utf-8').read()).call("encrypt", parama1, secretKey)
    print("captchaVerification----->"+captchaVerification)

    key,ticket = execjs.compile(open('finalCode.js', encoding='utf-8').read()).call("getKey", searchWord, publicKey)

    response = session.get("http://127.0.0.1:7001/get_sign?key=%s"%quote(key))
    sign = response.json()['sign']
    print("sign----->"+sign)
    print("ticket----->"+ticket)
    session.headers['sign'] = sign
    session.headers['ticket'] = ticket
    data = {"current":1,"size":5,"entity":{"keyAreasType":None,"heightLight":True,"opState":"","opYear":"","regOrg":"","licence":"","searchWord":searchWord,"searchType":"0","captchaVerification":captchaVerification,"captchaType":"blockPuzzle"}}
    r = session.post("http://gsxt.amr.gd.gov.cn/gsxt_gd/ent/base/list", data=json.dumps(data))
    # print(session.headers)
    print(r.json())

if __name__ == '__main__':
    searchWord = "91440400MA58AEL931"
    run(searchWord)


