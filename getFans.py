# 基于Pyppeteer库的爬虫
import asyncio
import time

import pyppeteer as pyp
import requests
import re


async def antiAntiCrawler(page):
    # 为page添加反反爬虫手段
    await page.setUserAgent('Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                            'AppleWebKit/537.36 (KHTML, like Gecko) '
                            'Chrome/98.0.4758.102 Safari/537.36 Edg/98.0.1108.62')
    await page.evaluateOnNewDocument(
        '() =>{ Object.defineProperties(navigator,'
        '{webdriver:{ get: () => false} }) }'
    )
    return page


async def getContent(url):
    width, height = 1400, 800  # 网页宽高
    browser = await pyp.launch(headless=False,
                               executablePath=r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe",
                               userDataDir=r'E:/地鼠Stitch/万粉抽奖/project/userdata',
                               args=[f'--window-size={width},{height}'])  # 启动浏览器
    page = await browser.newPage()  # 创建新页面
    page = await antiAntiCrawler(page)  # 为page添加反反爬虫手段
    await page.setViewport({'width': width, 'height': height})  # 设置网页宽高
    await page.goto(url, timeout=0)  # 进入网页

    input('请在准备好后点击回车')
    content = await page.content()
    result = re.findall(r'<div class="con "><div class="user"><a.*?>(.+?)</a>', content)

    # while True:
    #     content = await page.content()
    #     fans += re.findall(r'<span class="fans-name".*?>(.+?)</span>', content)
    #     print(len(fans))
    #     element = await page.querySelector('#page-follows > div > div.follow-main > div.follow-content.section > div.content > ul.be-pager > li.be-pager-next')
    #     time.sleep(0.5)
    #     if element:
    #         print(element)
    #         await element.click()
    #         time.sleep(0.3)
    #         await page.waitForSelector('#page-follows > div > div.follow-main > div.follow-content.section')
    #     else:
    #         break

    with open('评论视频的fans.txt', 'w', encoding='utf-8') as f:
        for name in result:
            f.write(name+'\n')
    await browser.close()


def getPictureOrVideo(url, file_name):
    r = requests.get(url, stream=True)
    with open(file_name, "wb") as f:
        f.write(r.content)


def main():
    # url = "https://t.bilibili.com/650442491948957699?tab=2"  # 动态
    # url = "https://space.bilibili.com/14892791/fans/fans"  # 粉丝
    # url = "https://message.bilibili.com/?spm_id_from=444.42.0.0#/love/124247558401"  # 点赞动态
    # url = "https://message.bilibili.com/?spm_id_from=444.42.0.0#/love/123836264477"  # 点赞配音员视频
    url = "https://www.bilibili.com/video/BV1RS4y1Y7H9"  # 配音员视频
    asyncio.get_event_loop().run_until_complete(getContent(url))


main()
