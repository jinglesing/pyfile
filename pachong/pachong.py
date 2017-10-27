# -*- coding:utf-8 -*-
__author__ = 'jinglesing'
# 1.普通爬虫方式
# 2.爬虫框架scrapy
# 3.爬取https://www.taptap.com
# 4.requests
# 5.BeautifulSoup

import requests
from bs4 import BeautifulSoup
gamenames ="王者荣耀"
def getlabels(games):
    url = 'https://www.taptap.com/search/apps?kw=%s'% gamenames
    session = requests.session()
    ret= session.get(url)
    print (ret.text)
    soup = BeautifulSoup(ret.text,"lxml")
    div = soup.find(class_="card-right-title")#b不是唯一的，正好是第一个就选了card-right-title
    print div.text.strip()
    next_url = div.attrs.get("href")
    print next_url

    ret = session.get(next_url)
    soup = BeautifulSoup(ret.text,"lxml")
    tagsob = soup.find(id= "appTag")#得到标签组
    links = tagsob.find_all('a')#得到所有标签的元素
    print type(links)
    tags = [link.text.strip() for link in links]#得到标签的文本
    print(tags)
    tag1 =links[0].text.strip()
    print tag1


getlabels(gamenames)