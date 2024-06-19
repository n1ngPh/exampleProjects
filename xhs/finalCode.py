import urllib.parse
import random
import math
import requests
import hashlib
import time
import random
import zlib
from urllib.parse import quote
import json
import execjs

# import subprocess
# from functools import partial #用来固定某个参数的固定值
# subprocess.Popen = partial(subprocess.Popen, encoding='utf-8')

# 防止直接调用，发包逻辑已删除


if __name__ == "__main__":
    xhs = XHS()
    xhs.get_activate()
    xhs.get_webprofile()
    xhs.get_homefeed()
    xhs.login()
    xhs.get_query("美食")

