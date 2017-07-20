#encoding=utf-8
from selenium import webdriver
import time
from Grobelmy import *
browser = webdriver.Chrome()
#建立操作浏览器的对象，来操作浏览器

browser.get("file:///D:/python/filepy/readandopen/indexone.html")
#等待非常重要
time.sleep(2)
#id是唯一的name不唯一，但id可能随机生成不能使用，要使用别的定位方式
browser.find_element_by_id('username').send_keys(username)
browser.find_element_by_id("passwood").send_keys(passwood)
browser.find_element_by_name("Submit").click()
time.sleep(2)