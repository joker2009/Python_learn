# -*-coding:UTF-8 -*-
import cookielib
import urllib2

# 保存cookie的本地磁盘文件名
filename = 'cookie.txt'

# 申明一个MozillaCookieJar(有save实现）对象示例来保存cookie,之后写入文件
cookiejar = cookielib.MozillaCookieJar(filename)

# 使用HTTPCookieProcessor()来创建cookie处理器对象，参数为CookieJar（）对象
handler = urllib2.HTTPCookieProcessor(cookiejar)

# 通过 build_opener()来构建opener
opener = urllib2.build_opener(handler)

# 创建一个请求，原理同urllib2的urlopen
response = opener.open("http://www.baidu.com")

# 保存cookie到本地文件
cookiejar.save()



