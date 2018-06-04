# -*- coding: UTF-8 -*-
import urllib2

# 构建一个HTTPHandler 处理器对象，支持处理HTTP请求
http_handler = urllib2.HTTPHandler(debuglevel=1)

# 调用urllib2.build_opener()方法，创建支持处理HTTP请求的opener对象
opener = urllib2.build_opener(http_handler)

# 构建Request请求
request = urllib2.Request("http://www.baidu.com/")

# 调用自定义opener对象的open()方法，发送reque请求
response = opener.open(request)

print(response.read())
