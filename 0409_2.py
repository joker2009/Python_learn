__author__ = 'Joker'
"""以下函数允许计算两个数的乘积，请稍加改造，变成可接收一个或多个数并计算乘积："""


def product(*arge):
    a = 1
    for i in arge:
        a = a * i
        # i *= i
    return a
t = (2, 2, 3, 8)

data = product(*t)
print(data)