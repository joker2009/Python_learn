__author__ = 'Joker'
# 斐波那契数列


def fab(max):
    n, a, b = 0, 0, 1
    # print(n)
    while n < max:
        # print(b)
        yield b
        a, b = b, a+b
        n += 1
    return "done"
# print(fab(7))
# for i in fab(6):
#     print(i)
# g = fab(6)
# while True:
#     try:
#         # next(fab(6))
#         print(next(g))
#     except StopIteration as error:
#         print(error.value)
#         break
"""杨辉三角其实就是上一列表相邻两数相加，再在头尾各填上一个1。
根据上述思路，不妨先设一个列表，L = [1]，剩下的就只需要用列表生成器生成出上一数组两数相加所得的列表。
在生成的列表上首位各拼接上一个为[1]的列表就好。
这里用到了一个技巧是range（n）会生成[0-n)的数，不包括n，当range（0）时，没有输出。
所以第一次遍历的时候中间的列表生成器其实是没有任何输出的，最后结果为[1,1]并不会报错。"""


def tri():
    L = [1]
    while True:
        yield L
        L = [1] + [L[i] + L[i+1] for i in range(len(L)-1)] + [1]
        # L = [1] + [L[i] for i in range(len(L)-1)] + [1]
        # L = [1] + [1]


n=0
for t in tri():
    print(t)
    n =n+1
    if  n==10:
        break

