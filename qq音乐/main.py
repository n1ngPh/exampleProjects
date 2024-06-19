import json
import requests
import time
import execjs
import random


def main():

    base_url = "https://u6.y.qq.com/cgi-bin/musics.fcg?_={}&sign={}"
    a = int(time.time() * 1000)
    guid = str(int((2147483647 * random.random()) * a % 1e10))
    data = {
        "comm": {
            "cv": 4747474,
            "ct": 24,
            "format": "json",
            "inCharset": "utf-8",
            "outCharset": "utf-8",
            "notice": 0,
            "platform": "yqq.json",
            "needNewCode": 1,
            "uin": 0,
            "g_tk_new_20200303": 5381,
            "g_tk": 5381
        },
        "req_1": {
            "module": "music.musicasset.SongFavRead",
            "method": "IsSongFanByMid",
            "param": {
                "v_songMid": [
                    "004Zw6rF17dkcF"
                ]
            }
        },
        "req_2": {
            "module": "music.musichallSong.PlayLyricInfo",
            "method": "GetPlayLyricInfo",
            "param": {
                "songMID": "004Zw6rF17dkcF",
                "songID": 493556698
            }
        },
        "req_3": {
            "method": "GetCommentCount",
            "module": "music.globalComment.GlobalCommentRead",
            "param": {
                "request_list": [
                    {
                        "biz_type": 1,
                        "biz_id": "493556698",
                        "biz_sub_type": 0
                    }
                ]
            }
        },
        "req_4": {
            "module": "music.musichallAlbum.AlbumInfoServer",
            "method": "GetAlbumDetail",
            "param": {
                "albumMid": "0000oWWx1m0XT4"
            }
        },
        "req_5": {
            "module": "vkey.GetVkeyServer",
            "method": "CgiGetVkey",
            "param": {
                "guid": guid,
                "songmid": [
                    "004Zw6rF17dkcF"
                ],
                "songtype": [
                    0
                ],
                "uin": "0",
                "loginflag": 1,
                "platform": "20"
            }
        }
    }
    data = json.dumps(data, separators=(',', ':'))
    # print(data)
    headers = {
    'accept': 'application/json',
    'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8',
    'cache-control': 'no-cache',
    'content-type': 'application/x-www-form-urlencoded',
    'cookie': 'pgv_pvid=4133268380; fqm_pvqid=1310c331-0c1f-4609-bcde-20a23a297a12; fqm_sessionid=4bf3ee88-a6dc-4f80-b187-80d99a61dd14; pgv_info=ssid=s2903741396; ts_uid=4411813700; _qpsvr_localtk=0.972755850534625; ts_last=y.qq.com/n/ryqq/player',
    'origin': 'https://y.qq.com',
    'pragma': 'no-cache',
    'priority': 'u=1, i',
    'referer': 'https://y.qq.com/',
    'sec-ch-ua': '"Google Chrome";v="125", "Chromium";v="125", "Not.A/Brand";v="24"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36'
    }
    ts = int(time.time() * 1000)
    sign = execjs.compile(open('qq.js', encoding="utf-8").read()).call("get_sign", data)
    url = base_url.format(ts, sign)
    response = requests.post(url, headers=headers, data=data)
    print(response.text)

main()