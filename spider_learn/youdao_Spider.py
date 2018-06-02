__author__ = 'joker_jiang'

import urllib
import urllib2

# POST请求的目标URL
url = "http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule&smartresult=ugc&sessionFrom=null"

headers= {"User-Agent": "Mozilla..."}

formdata = {
    "type": "AUTO",
    "i": "i love python",
    "doctype": "json",
    "xmlVersion": "1.8",
    "keyfrom": "fanyi.web",
    "ue": "UTF-8",
    "action": "FY_BY_ENTER",
    "typoResult": "true"
}

data = urllib.urlencode(formdata)

request = urllib2.Request(url, data = data, headers= headers)
response = urllib2.urlopen(request)
print(response.read())

