import requests
from bs4 import BeautifulSoup
import re
import xiguainfo
import RSS
import xiangjiaoinfo
import os

def getwell():
    """获取输入数据"""
    well = RSS.getmessage
    if well == str(1):
        xiguainfo.getxiguainfo()
        xiguainfo.getxiguaurl()
    else:
        xiangjiaoinfo.getxiangjiaoinfo()
        xiangjiaoinfo.getxiangjiaourl()


if __name__ == '__main__':
    getwell()
    try:
        os.remove()