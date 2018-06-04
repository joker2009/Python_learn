# -*- coding:UTF-8 -*-
import requests

# formdata = {
#     "type": "AUTO",
#
# }

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
url = "http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule&smartresult=ugc&sessionFrom=null"
headers = {
"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) Apple WebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36"}

response = requests.post(url, data= formdata, headers= headers)
print(response.text)

print(response.json())