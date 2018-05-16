def char2num(s):
    digits = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
    return digits[s]


# a = map(char2num, '13474')
# print(a)
# for i in a:
#     print(i)
"""利用map()函数，把用户输入的不规范的英文名字，变为首字母大写，其他小写的规范名字。输入：['adam', 'LISA', 'barT']，输出：['Adam', 'Lisa', 'Bart']："""


def normalize(name):
    name = str.title(name)
    return name


#
# def normalize(name):
#     def capital(str):
#         return str.capitalize()
#     return map(capital, name)

# 测试:


# L1 = ['adam', 'LISA', 'barT']
# # L2 = list(map(normalize, L1))
# #
# # print(L2)

"""Python提供的sum()函数可以接受一个list并求和，请编写一个prod()函数，可以接受一个list并利用reduce()求积："""
from functools import reduce


def prod(list):
    def res(a, b):
        return a * b

    return reduce(res, list)


# a = [1, 3, 4, 8]
# # prod(a)
# print(prod(a))
"""利用map和reduce编写一个str2float函数，把字符串'123.456'转换成浮点数123.456："""

s = '123.456'
# def charm2num(s):
#     DIGITS = {'1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '0': 0}
#     return DIGITS[s]


def num2float(x, y):
    return x * 10 + y


str1, str2 = s.split('.')
f1 = reduce(num2float, map(char2num, str1))
print(f1)
f2 = reduce(num2float, map(char2num, str2))
print(f2/pow(10, len(str2)))
f = f1+f2/pow(10, len(str2))
print(type(f))
print(f)

