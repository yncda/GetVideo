#coding: UTF-8
import requests
from bs4 import BeautifulSoup
import re
import os
import RSS

def getxiguainfo():
    """获取西瓜视频网页视频信息"""
    # 模拟安卓UA
    headers = {
        'User-Agent': 'Mozilla/5.0 (Linux; Android 4.4.2; Nexus 4 Build/KOT49H) AppleWebKit/537.36 '
                      '(KHTML, like Gecko) Chrome/34.0.1847.114 Mobile Safari/537.36'}
    # 定义网址
    url = 'http://itrafficnet.com/api/videosort/47?orderby=&page={{page}}'
    # 获取网页信息
    r = requests.get(url, timeout=60, headers=headers)
    soup = BeautifulSoup(r.text, 'lxml')
    # 获取网页内容
    result = soup.select('body')
    # 网页内容中匹配页码
    Regular3 = r'last_page":\d+'
    Regular_expression3 = re.compile(Regular3)
    htmlpages = Regular_expression3.findall(str(result[0]))
    # 匹配最终页码
    Regular4 = r'\d+'
    Regular_expression4 = re.compile(Regular4)
    pages = Regular_expression4.findall(htmlpages[0])
    # 网页内容中匹配网址
    Regular5 = r'next_page_url":".*page='
    Regular_expression5 = re.compile(Regular5)
    datas = Regular_expression5.findall(str(result[0]))
    Regular6 = r'http:.*page='
    Regular_expression6 = re.compile(Regular6)
    data = Regular_expression6.findall(datas[0])
    page_url = data[0].replace('\\', '')
    if os.path.isdir("视频链接"):
        pass
    else:
        os.mkdir("视频链接")
    with open('视频链接/xiguapages.txt', 'w') as p:
        for page in range(1, int(pages[0]) + 1):
            p.write(page_url + str(page)+'\n')
