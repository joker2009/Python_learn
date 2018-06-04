# -*- coding:UTF-8 -*-
import urllib
import urllib2
import cookielib

# 构建一个CookieJar对象实例来保存cookie
cookie = cookielib.CookieJar()

# 使用HTTPCookieProcessor()来创建cookie处理器对象，参数为CookieJar()对象
cookie_handler = urllib2.HTTPCookieProcessor(cookie)

# 通过build_opener()来构建opener
opener = urllib2.build_opener(cookie_handler)

# addheader 接受一个列表，里面每个元素都是一个Headers信息的元祖，opener将附带headers信息
opener.addheaders = [("User-Agent", "Mozilla/5.0 (Windows NT 10.0;Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36")]

#  需要登录的账号和密码
data = {"email": '304640509@qq.com', "password": "1234abc5678+"}

# 通过urlencode()转码
postdata = urllib.urlencode(data)

# 构建Request请求对象，包含需要发送的用户名和密码
request = urllib2.Request("http://www.renren.com/PLogin.do", data= postdata)

# 通过opener发送这个请求，并获取登录后的COOKIE值
opener.open(request)

# opener 包含用户登录后的Cookie值，可以直接访问那些登录后才可以访问的页面
response = opener.open("http://www.renren.com/410043129/profile")

print(response.read())
