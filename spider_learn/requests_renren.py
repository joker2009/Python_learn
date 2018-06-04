# -*- coding:UTF-8 -*-
import requests

# 创建session对象，可以保存Cookie值
ssion = requests.session()

# 处理headers
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36"}

# 需要登录的用户名和密码
data = {"email": "304640509@qq.com", "password": "1234abc5678+"}

# 发送附带用户名和密码的请求，并获取登录后的Cookie值，保存在ssion
ssion.post("http://www.renren.com/PLogin.do", data=data)

# ssion包含用户登录后的Cookie值，可以直接访问哪些登录后才可以访问的页面
response = ssion.get("http://www.renren.com/410043129/profile")

print(response.text)