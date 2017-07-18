#encoding=utf-8
from selenium import webdriver
'''
from selenium
browser = selenium.webdriver.Chrome()

'''
#browser为对象，（）函数，方法，元祖，
browser = webdriver.Chrome()#建立操作浏览器的对象，来操作浏览器

browser.get("https://www.baidu.com/")

browser.find_element_by_xpath('//*[@id="kw"]').send_keys("selenium")
browser.find_element_by_id("su").click()