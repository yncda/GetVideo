#coding: UTF-8
import requests
from bs4 import BeautifulSoup
import re
import os
import json

def get_pageinfo():
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
    Regular1 = r'last_page":\d+'
    Regular_expression1 = re.compile(Regular1)
    htmlpages = Regular_expression1.findall(str(result[0]))
    # 匹配最终页码
    Regular2 = r'\d+'
    Regular_expression2 = re.compile(Regular2)
    pages = Regular_expression2.findall(htmlpages[0])
    # 网页内容中匹配网址
    Regular3= r'next_page_url":".*page='
    Regular_expression3 = re.compile(Regular3)
    datas = Regular_expression3.findall(str(result[0]))
    Regular4 = r'http:.*page='
    Regular_expression4 = re.compile(Regular4)
    data = Regular_expression4.findall(datas[0])
    page_url = data[0].replace('\\', '')
    if os.path.isdir("视频链接"):
        pass
    else:
        os.mkdir("视频链接")
    with open('视频链接/xiguapages.json', 'w') as p:
        for page in range(1, int(pages[0]) + 1):
            json.dump(page_url + str(page),p)
            p.write('\n')


def get_url():
    """获取西瓜视频m3u8链接"""
    # 模拟安卓UA
    headers = {
        'User-Agent': 'Mozilla/5.0 (Linux; Android 4.4.2; Nexus 4 Build/KOT49H) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/34.0.1847.114 Mobile Safari/537.36'}

    with open('视频链接/xiguapages.json', 'r') as p:
        urlline = p.readlines()
        for url in urlline:
            #定义网址
            url = url
            #获取网页信息
            r = requests.get(url, timeout=60, headers=headers)
            soup = BeautifulSoup(r.text, 'lxml')
            #获取网页内容
            result = soup.select('body')
            #正则表达式匹配查找id
            Regular5 = r'id":\d+'
            Regular_expression5 = re.compile(Regular5)
            #网页内容中匹配id内容
            datas = Regular_expression5.findall(str(result[0]))
            # id内容中匹配id
            Regular6 = r'\d+'
            Regular_expression6 = re.compile(Regular6)
            ids = Regular_expression6.findall(str(datas))
            Regular7 = r'\'
            with open('视频链接/xiguaid.txt', 'a') as p:
                for id in ids:
                    p.write(page_url+str(id)+'?'+xiguauuid+'\n')

def get_videourl():
    # 模拟安卓UA
    headers = {
        'User-Agent': 'Mozilla/5.0 (Linux; Android 4.4.2; Nexus 4 Build/KOT49H) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/34.0.1847.114 Mobile Safari/537.36'}
    html = getxiguainfo()
    page_url = 'http://itrafficnet.com/api/videoplay/'
    xiguauuid = 'uuid=84fc81a928ee5e58'
    with open('视频链接/xiguapages.json', 'r') as p:
        urlline = p.readlines()
        for url in urlline:
            # 定义网址
            url = url
            # 获取网页信息
            r = requests.get(url, timeout=60, headers=headers)
            soup = BeautifulSoup(r.text, 'lxml')
            # 获取网页内容
            result = soup.select('body')
            # 正则表达式匹配查找id
            Regular1 = r'id":\d+'
            Regular_expression1 = re.compile(Regular1)
            # 网页内容中匹配id内容
            datas = Regular_expression1.findall(str(result[0]))
            # id内容中匹配id
            Regular2 = r'\d+'
            Regular_expression2 = re.compile(Regular2)
            ids = Regular_expression2.findall(str(datas))
            #
            #

            #     for data in datas:
            #         id = Regular_expression2.findall(str(data))
            #         p.write(page_url + str(page) + '\n')
            with open('视频链接/xiguaid.txt', 'a') as p:
                for id in ids:
                    p.write(page_url + str(id) + '?' + xiguauuid + '\n')