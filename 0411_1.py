__author__ = 'Joker'


def trim(s):

    if not isinstance(s, str):
        raise TypeError("类型错误")
    print(s[0])
    print(s[-1])

    if s[0] == " ":

        print(s[0])
        s = s[1]
        # while s[0] != " ":
        #     return s
    if s[-1] == " ":
        s = s[-2]
        # while s[-1] != " ":
    return s
# 测试:
if trim('hello  ') != 'hello':
    print('测试失败!')
elif trim('  hello') != 'hello':
    print('测试失败!')
elif trim('  hello  ') != 'hello':
    print('测试失败!')
elif trim('  hello  world  ') != 'hello  world':
    print('测试失败!')
elif trim('') != '':
    print('测试失败!')
elif trim('    ') != '':
    print('测试失败!')
else:
    print('测试成功!')