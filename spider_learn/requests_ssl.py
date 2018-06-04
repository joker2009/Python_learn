import requests

response = requests.get("http://www.12306.cn/mormhweb", verify=True)
print(response.text)