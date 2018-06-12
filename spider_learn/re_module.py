# -*- coding:UTF-8 -*-
import re
# pattern = re.compile(r'\d+')  # 匹配至少一个数字
#
# m = pattern.match('one12twothree34four')  # 查找头部，没有匹配
# print(m)

# pattern = re.compile(r'([a-z]+) ([a-z]+)', re.I)
# m = pattern.match('hello world Wide Web')
#
# print(m)
#
# print(m.group(0))
# print m.span(0)
# print m.group(1)
# print m.group(2)
# print m.span(2)
# print m.groups()


# pattern = re.compile(r'\d+')
# m = pattern.search('hello 123456 789')
# if m:
#     print('matching string', m.group())
#     print('position:', m.span())

pattern = re.compile(r'\d\.\d*')

result = pattern.findall("123.1411593, 'bigcat', 232323, 3.15")

for item in result:
    print(item)


