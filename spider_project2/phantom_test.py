# -*- coding:utf-8-*-
# IPython 测试代码

# 导入 webdriver
from selenium import webdriver

# 调用环境变量指定的PhantomJS浏览器创建浏览器对象
# driver = webdriver.PhantomJS()

# 如果没有在环境变量制定PhantomJS位置
driver = webdriver.PhantomJS(executable_path=r"D:\phantomjs\phantomjs-1.9.2-windows\phantomjs-1.9.2-windows\phantomjs.exe")

# get方法会一直等到页面被完全加载，然后才会继续程序，通常测试会在这里选择 time.sleep(2)
driver.get("http://www.baidu.com/")

# 获取页面名为wrapper的id标签的文本内容
data = driver.find_element_by_id("wrapper").text

print(data)

print(driver.title)

driver.save_screenshot("baidu.png")
driver.find_element_by_id("kw").send_keys(u"长城")

driver.find_element_by_id("su").click()

driver.save_screenshot("great_wall.png")
print(driver.page_source)
# 获取当前页面的Cookie
print(driver.get_cookies())

# 调用键盘按键操作时需要引入的Keys包
from selenium.webdriver.common.keys import Keys

# ctrl+ a 全选输入框内容
driver.find_element_by_id("kw").send_keys(Keys.CONTROL,'a')

# ctrl+x 剪切输入框内容
driver.find_element_by_id("kw").send_keys(Keys.CONTROL,'x')

driver.find_element_by_id("kw").clear()
# 获取新的页面快照
driver.save_screenshot("itcast.png")
# 获取当前URL
print(driver.current_url)

# 关闭当前页面，如果只有一个页面，会关闭浏览器
driver.close()

# 关闭浏览器
driver.quit()
