# -*- coding:utf-8 -*-
# @Time : 2022/4/26 17:37
# @File : test.py
# @Software : PyCharm

from fake_useragent import UserAgent
import os
import asyncio
import aiofiles
import aiohttp
import gotoMySQL

"""
获取mysql库里的海报连接，然后异步下载。
有些海报会下载失败，则需要手动保存到img文件夹下。
"""

async def pic_download(url, session, headers):
    imgPath = f'./static/img/{url.split("/")[-1]}'
    if not os.path.exists(imgPath):
        try:
            async with session.get(url, headers=headers) as resp:
                async with aiofiles.open(imgPath, mode='wb') as f:
                    await f.write(await resp.content.read())
                    resp.close()
        except:
            print(f"Error:{url}\n")


async def downImg(pic):
    timeout = aiohttp.ClientTimeout(total=600)  # 将超时时间设置为600秒
    connector = aiohttp.TCPConnector(limit=50)  # 将并发数量降低
    tasks = []
    ua = UserAgent()
    headers = {'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.64 Safari/537.36 Edg/101.0.1210.53"}
    async with aiohttp.ClientSession(timeout=timeout, connector=connector) as session:
        for url in pic:
            task = asyncio.create_task(pic_download(url, session, headers))
            tasks.append(task)
        await asyncio.wait(tasks)

def main():
    data = gotoMySQL.GotoMySQL(0).readMysql()
    pic = []
    for i in data:
        pic.append(i[6])

    loop = asyncio.get_event_loop()
    loop.run_until_complete(downImg(pic))

main()