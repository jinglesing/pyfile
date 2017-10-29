# -*- coding:utf-8 -*-
__author__ = 'jinglesing'
# 1.普通爬虫方式
# 2.爬虫框架scrapy
# 3.爬取https://www.taptap.com
# 4.requests
# 5.BeautifulSoup、lxml--解析html
# 6.打印一整页

import requests
from bs4 import BeautifulSoup
import json
session = requests.session()#表示创建一个连接
gamenames ="王者荣耀"
def getlabels(games):
    url = 'https://www.taptap.com/search/apps?kw=%s'% gamenames
    ret= session.get(url)
    # print (ret.text)#网页源代码
    soup = BeautifulSoup(ret.text,"lxml")
    divs = soup.find_all(class_="card-right-title")#find_all查找全部
    print divs
    for div in divs:
        print div.text.strip()
        next_url = div.attrs.get("href")#从属性里面获得href从而得到网址
        print next_url
        ret = session.get(next_url)
        soup = BeautifulSoup(ret.text,"lxml")#lxml要pip安装
        tagsob = soup.find(id= "appTag")#得到标签组
        links = tagsob.find_all('a')#得到所有标签的元素

        tags = [link.text.strip() for link in links]#得到标签的文本
        print json.dumps(tags,encoding="utf-8",ensure_ascii=False)#为了输出中文


getlabels(gamenames)

#如何显示更多