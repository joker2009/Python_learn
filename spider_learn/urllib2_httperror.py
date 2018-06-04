import urllib2

request = urllib2.Request("http://www.itcast.cn/blog")

try:
    urllib2.urlopen(request)
except urllib2.HTTPError, error:
    print(error.code)
    print(error)