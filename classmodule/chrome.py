#!/usr/bin/python3
#conding=utf-8

from selenium import webdriver
from time import sleep

webdriver = webdriver.Chrome()
webdriver.get("https://www.baidu.com/?tn=baiduerr")
webdriver.maximize_window()
webdriver.find_element_by_id("kw").send_keys("Selenium")
webdriver.find_element_by_id("su").click()

sleep(10)
webdriver.quit()
