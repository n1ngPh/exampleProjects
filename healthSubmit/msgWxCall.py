import json
import requests
from loguru import logger


class wxMsgCom:
    def __init__(self, corpid, corpsecret, agentid):
        self._http = requests.session()
        self._http.headers = {
        }
        self._host = "https://qyapi.weixin.qq.com/cgi-bin/"
        self._corpid = corpid
        self._corpsecret = corpsecret
        self._agentid = agentid

    def getAccessToken(self):
        res = self._http.get(
            url="{0}gettoken?corpid={1}&corpsecret={2}".format(self._host, self._corpid, self._corpsecret))
        try:
            ret = json.loads(res.text)
            self._access_token = ret["access_token"]
        except json.JSONDecodeError:
            logger.error("Messages do not seem to be parsed correctly")

    def _sendMessage(self, obj):
        jData = json.dumps(obj, ensure_ascii=False).encode('utf-8')
        res = self._http.post(url="{0}message/send?access_token={1}".format(self._host, self._access_token), data=jData)
        try:
            ret = json.loads(res.text)
            errmsg = ret["errmsg"]
        except json.JSONDecodeError:
            logger.error("Messages do not seem to be parsed correctly")
        if errmsg == "ok":
            logger.info("Alert notice")
        else:
            logger.error(ret)



    def sendTextMessage(self, touser, content):
        jData = {
            "touser": touser,
            "toparty": "",
            "totag": "",
            "msgtype": "text",
            "agentid": self._agentid,
            "text": {
                "content": content
            },
            "safe": 0,
            "enable_id_trans": 0,
            "enable_duplicate_check": 0,
            "duplicate_check_interval": 1800
        }
        self._sendMessage(jData)


    def sendTextCardMessage(self, touser, title, description, url="", btntxt="更多"):
        """

        :param touser:推送用户
        :param title:标题
        :param description: 描述 <div class=\"normal\"></div> <div class=\"gray\"></div> <div class=\"highlight\"></div>
        :param url:点击前往链接
        :param btntxt:按钮名称
        :return:None
        """
        jData = {
            "touser": touser,
            "toparty": "",
            "totag": "",
            "msgtype": "textcard",
            "agentid": self._agentid,
            "textcard": {
                "title": title,
                "description": description,
                "url": url,
                "btntxt": btntxt
            },
            "safe": 0,
            "enable_id_trans": 0,
            "enable_duplicate_check": 0,
            "duplicate_check_interval": 1800
        }
        self._sendMessage(jData)

    def sendMarkdownMessage(self, touser, content):
        """

        :param touser: 推送用户
        :param content: 推送内容
        :return: None
        """
        jData = {
            "touser": touser,
            "toparty": "",
            "totag": "",
            "msgtype": "markdown",
            "agentid": self._agentid,
            "markdown": {
                "content": content
            },
            "enable_duplicate_check": 0,
            "duplicate_check_interval": 1800
        }
        self._sendMessage(jData)

