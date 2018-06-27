# -*- coding:utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome(executable_path=r"D:\phantomjs\chromedriver.exe")
driver.get("http://www.douban.com")

# 输入账号密码
driver.find_element_by_name("form_email").send_keys("304640509@qq.com")
driver.find_element_by_name("form_password").send_keys("1234abc5678+")

# 模拟点击登陆
driver.find_element_by_xpath("//input[@class='bn-submit']").click()

time.sleep(3)

# 生成登陆后快照
driver.save_screenshot("douban.png")

# 保存源码
with open("douban.html","w") as file:
    file.write(driver.page_source)

driver.quit()
