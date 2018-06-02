__author__ = 'joker_jiang'
import urllib2
url = "https://movie.douban.com/j/chart/top_list?type=11&interval_id=100%3A90&action=&"

headers = {"User-Agent": "Mozilla...."}

# 变动的是这两个参数，从star开始往后显示limit个

formdata = {
    'start': '0',
    'limit': '10'
}
data = urllib.urlencode(formdata)

request = urllib2.Request(url + data, headers=headers)

response = urllib2.urlopen(request)

print(response.read())