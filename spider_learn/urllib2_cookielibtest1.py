# -*- coding:UTF-8 -*-

import urllib2
import cookielib

# 构建一个CookieJar对象示例来报错cookie
cookiejar = cookielib.CookieJar()

# 使用HTTPCookieProcessor()来创建cookie处理器对象，参数为CookieJar()对象
handler = urllib2.HTTPCookieProcessor(cookiejar)

# 通过 build_opener()来构建opener
opener = urllib2.build_opener(handler)

# 以get方法访问页面，访问之后会自动保存cookie到cookiejar中
opener.open("http://www.baidu.com")

# 可以按照标准格式将保存的Cookie打印出来
cookieStr = ""

for item in cookiejar:
    cookieStr = cookieStr + item.name + "=" + item.value+";"

print cookieStr[:]