import urllib2

url = "http://www.itcast.cn"

user_agent = {"User-Agent" : "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0)"}

request = urllib2.Request(url, headers=user_agent)

request.add_header("Connection", "Keep-alive")
request = urllib2.urlopen(request)
print(request.code)
html = request.read()
print(html)