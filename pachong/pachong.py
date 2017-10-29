# -*- coding:utf-8 -*-
__author__ = 'jinglesing'
# 1.普通爬虫方式
# 2.爬虫框架scrapy
# 3.爬取https://www.taptap.com
# 4.requests
# 5.BeautifulSoup、lxml--解析html

import requests
import json
from bs4 import BeautifulSoup
gamenames ="勇者荣耀"
def getlabels(games):
    url = 'https://www.taptap.com/search/apps?kw=%s'% gamenames
    session = requests.session()#表示创建一个连接
    ret= session.get(url)
    print (ret.text)#网页源代码
    soup = BeautifulSoup(ret.text,"lxml")
    # 如果是第二个怎么办
    #    div = soup.find_all(class_="card-right-title")[1]
    div = soup.find(class_="card-right-title")#不是唯一的，正好是第一个就选了card-right-title、class是关键字用class_来代替
    print div.text.strip()
    next_url = div.attrs.get("href")#从属性里面获得href从而得到网址
    print next_url

    ret = session.get(next_url)
    soup = BeautifulSoup(ret.text,"lxml")#lxml要pip安装
    tagsob = soup.find(id= "appTag")#得到标签组
    links = tagsob.find_all('a')#得到所有标签的元素
    print type(links)#class
    tags = [link.text.strip() for link in links]#得到标签的文本
    print(tags)
    print json.dumps(tags, encoding="utf-8", ensure_ascii=False)  # 为了输出中文
    tag1 =links[0].text.strip()#strip()去空格
    print type(tags)#list
    print tag1


getlabels(gamenames)