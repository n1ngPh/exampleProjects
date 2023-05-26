import time
import datetime
import requests
import rapidjson as json
import math
import random
from urllib.parse import quote
from loguru import logger as console
import msgWxCall


def getYesterday():
    """取昨天日期"""
    yesterday = datetime.date.today() + datetime.timedelta(-1)
    return yesterday


def _getFmtTime():
    return time.strftime('%Y年%m月%d日', time.localtime(time.time()))


def getmsUnixStr():
    """获取13位时间戳"""
    return str(math.floor(time.time() * 1000))


def getGuid(formats="", length=32):
    """生成一个 Guid(全球唯一标识符) 值；该函数定义如下参数：
    format: String 类型值，一个单格式说明符，它指示如何格式化此 Guid 的值。?format 参数可以是：
            "N":    返回值的格式 32 位(xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx)
            "D":    返回值的格式 由连字符分隔的 32 位数字(xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx)
            "B":    返回值的格式 括在大括号中、由连字符分隔的 32 位数字({xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx})
            "P":    返回值的格式 括在圆括号中、由连字符分隔的 32 位数字((xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx))
            如果 format 为 null 或空字符串 ("")，则使用 "D"。
    length: Number 类型值，表示返回字符串的长度；如果不定义该参数，则全部返回。"""
    if formats == "":
        formats = "n"
    else:
        formats = formats.lower()
    if length < -32:
        length = -32
    ret = ""

    for i in range(1, 33):
        ret += hex(math.floor(random.random() * 16.0))[2:]
        if (i == 8) or (i == 12) or (i == 16) or (i == 20):
            ret += "-"
        if formats == "n":
            ret = ret.replace("-", '')
            continue
        elif formats == "b":
            ret = "{" + ret + "}"
            continue
        elif formats == "p":
            ret = "(" + ret + ")"
            continue
        elif formats == "d":
            continue
    if length >= 0:
        ret = ret[:length]
    else:
        ret = ret[:-abs(length)]
    return ret


class StdInfo:
    def __init__(self, cookie, corpid="", corpsecret="", agentid=0, touser=""):
        """
        :param cookie: 用户标识
        :param corpid: 企业ID
        :param corpsecret: 企业Secret
        :param agentid: 插件ID
        :param touser: 推送用户
        """
        # 企业微信推送API初始化
        self.wxMsg = None
        if corpid != "" and corpsecret != "" and agentid != 0 and touser != "":
            self.wxMsg = msgWxCall.wxMsgCom(corpid, corpsecret, agentid)
            self.wxMsg.getAccessToken()
            self.touser = touser

        self.http = requests.session()  # 启用session
        console.debug("Create requests session.")
        self.cookie = requests.utils.cookiejar_from_dict(cookie)  # 解析cookie转换成cookiejar类型
        self.headers = {
        }  # 初始化协议头
        self.http.cookies = self.cookie  # cookie置入
        console.debug("cookies set successfully")
        self.http.headers = self.headers  # 协议头置入
        console.debug("headers set successfully")

        models = [
            '2cd898ec1e394ab1a4c7c539a41a1487', '663b29fd97cf44c399a933e8e71cec89', '08e034eda88049a7b476c4f223e9a947']
        self.TableId = models[0]  # 表串 用于多表的提交
        self.initInfo()  # 初始化,获取用户数据
        console.success("Setting TableId: {0}".format(self.TableId))

        self.getDate()

    def initInfo(self):
        """取必要的用户数据"""
        url = "http://ehallwx.ypc.edu.cn/Pages/Detail.aspx?ID={0}".format(self.TableId)
        res = self.http.get(url=url)
        console.debug("HttpCode: {0}".format(str(res.status_code)))
        if res.status_code != 200:
            console.error("Failed to access the interface. Please check if the cookie is valid.")
        ret = res.text
        start = ret.find('"USERID": "')
        end = ret.find('",', start)
        self.USERID = ret[start + 11:end]  # 用户标识符的置入
        console.success("Setting ID: {0}".format(self.USERID))

        start = ret.find('FORMID:"')
        end = ret.find('",', start)
        self.FORMID = ret[start + 8:end]  # 用户序列号(学号 的置入
        console.success("Setting FORMID: {0}".format(self.FORMID))

        start = ret.find('GUID:"')
        end = ret.find('",', start)
        self.GUID = ret[start + 6:end]  # 唯一标识符的置入
        console.success("Setting GUID: {0}".format(self.GUID))

    def sqlQuery(self, key):
        """Sql查询接口，用于统一接口的快速查询"""
        url = "http://ehallwx.ypc.edu.cn/Popup/TaskHandler.ashx"
        data = "Action=exesql&strSQLKey={0}&flag=Query&t=".format(key) + \
               getmsUnixStr()
        res = self.http.post(url=url, data=data)
        console.debug("HttpCode: {0}".format(str(res.status_code)))
        if res.status_code != 200:
            console.error("Code: {0} Failed to access the interface. Please check if the cookie is valid.".format(str(
                res.status_code
            )))
        ret = res.text
        return ret

    def extractInfo(self):
        """取昨日提交记录"""
        key = "SYS_SJYZ%24{0}%7E{1}".format(self.USERID, getYesterday())
        ret = self.sqlQuery(key)
        try:
            ret = json.loads(ret)[0]
        except IndexError:
            console.error("IndexError {0}".format(ret))
        self.yestData = ret  # 昨日提交信息的置入
        console.info("yestData was retrieved successfully")

    def getDate(self):
        """获取服务器时间/日期"""
        key = "SELECT_GETDATE%2524"
        ret = self.sqlQuery(key)
        try:
            ret = json.loads(ret)[0]

        except IndexError:
            console.error("IndexError {0}".format(ret))
        self.time = ret["nowtime"]  # 服务器时间的置入
        self.date = ret["nowdate"]  # 服务器日期的置入
        console.info("WebSites Date was retrieved successfully {0}".format(self.time))

    def generate(self):
        """生成提交数据"""
        self.extractInfo()
        self.yestData["GUID"] = self.GUID  # 参数 GUID 的重新置入
        self.yestData["YQ_SBRQ"] = self.date  # 参数 YQ_SBRQ 的重新置入
        self.yestData["BZSJ"] = self.time  # 参数 BZSJ 的重新置入
        self.yestData["YQDATE"] = self.date  # 参数 YQDATE 的重新置入
        self.yestData["YQ_DRTW"] = "36." + str(random.randint(4, 8))  # 参数 YQ_DRTW 的随机生成

        console.info("Set the temperature {0}℃".format(self.yestData["YQ_DRTW"]))

        self.data = {
            "main": [
                {
                    "TableName": "PROC_YQBS",
                    "Data": [self.yestData],
                    "TableId": self.TableId
                }
            ],
            "sub": [],
            "LoginUserID": self.USERID,
            "GUID": self.GUID,
            "FORMID": self.FORMID
        }  # 构造提交json数据
        self.data = json.dumps(self.data, ensure_ascii=False)
        console.success("data generation successful")

    def submit_model(self):
        """健康数据提交"""
        self.generate()
        url = ""
        res = self.http.post(url=url, data=self.data.encode('utf-8'))
        console.debug("HttpCode: {0}".format(str(res.status_code)))
        ret = res.text
        msg = ""
        try:
            jData = json.loads(ret)
            msg = jData["msg"]
            jData = json.dumps(jData,ensure_ascii=False)
        except json.JSONDecodeError:
            console.error("It doesn't seem to work")
        # 推送
        if self.wxMsg is not None and not msg.startswith("提交成功"):
            self.wxMsg.sendTextMessage(self.touser, "貌似出错了\n{0}".format(jData))
        else:
            self.wxMsg.sendTextMessage(self.touser, "提交成功\n{0}".format(jData))
        console.info(ret)


    def report(self):
        """查询当日是否已提交"""
        key = "SYS_SJYZ%2524{0}%257E{1}".format(quote(self.USERID), self.date)
        ret = self.sqlQuery(key)
        if ret == "[]":
            self.submit_model()
        else:
            console.warning("It has been reported today. Please do not submit it again {0}".format(self.time))
            # 推送
            if self.wxMsg is not None:
                self.wxMsg.sendTextMessage(self.touser, "今日已打卡")





def Main():
    # 填写Cookie
    cookies = {}
    cls = StdInfo(cookie=cookies, corpid="",
                  corpsecret="", agentid=, touser="N")
    cls.report()


Main()
