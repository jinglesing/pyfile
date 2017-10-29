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
import time
session = requests.session()#表示创建一个连接
gamenames ="王者荣耀"
def getlabels(games):
    url2 = 'https://www.taptap.com/ajax/search/apps?kw=%s&page=2'% gamenames
    ret= session.get(url2)
    print ret.text
    print type(ret)
    time.sleep(1)
    datas = ret.json()["data"]
    html_is = datas["html"]
    neturl_is = datas["next"]
    soup = BeautifulSoup(html_is,"lxml")
    all_links = soup.find_all(class_="card-tags")#find_all查找所以的标签层

    for link in all_links:
        ass =  link.find_all("a")#每一层找所有的标签、
        tags=[link.text.strip() for link in ass]
        # print tags
        print json.dumps(tags, encoding="utf-8", ensure_ascii=False)  # 为了输出中文
    while neturl_is:
        print neturl_is
        ret = session.get(neturl_is)
        datas = ret.json()["data"]
        html_is = datas["html"]
        neturl_is = datas["next"]
        soup = BeautifulSoup(html_is, "lxml")
        all_links = soup.find_all(class_="card-tags")  # find_all查找所以的标签层
        links =soup.find(class_ ="card-right-title")
        print links.text.strip()
        for link in all_links:

            ass = link.find_all("a")  # 每一层找所有的标签、
            tags = [link.text.strip() for link in ass]
            # print tags
            print json.dumps(tags, encoding="utf-8", ensure_ascii=False)  # 为了输出中文




getlabels(gamenames)

#如何显示更多