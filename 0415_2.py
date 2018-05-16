
"""计算素数的一个方法是埃氏筛法，它的算法理解起来非常简单"""
"""首先构造一个奇数序列，
判断是否整除
使用filter过滤序列
设置一个退出值"""


def _odd_iter():
    n = 1
    while True:
        yield n
        n = n + 2
        # yield n


def _not_is_div(n):
    return lambda x: x % n > 0


# def primes():
#     yield 2
#     it = _odd_iter()  # 初始化序列
#     while True:
#         n = next(it)  # 返回序列的第一个数
#         yield n
#         it = filter(_not_is_div, it)  # 构造新序列


# it = _odd_iter()
# n = 1
# for i in it:
#     print(i)


"""回数是指从左向右读和从右向左读都是一样的数，例如12321，909。请利用filter()筛选出回数："""


def is_palindrome(n):
    return str(n) == str(n)[::-1]


# # 测试:
# output = filter(is_palindrome, range(1, 1000))
# print('1~1000:', list(output))
# if list(filter(is_palindrome, range(1, 200))) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 22, 33, 44, 55, 66, 77, 88, 99, 101, 111, 121, 131, 141, 151, 161, 171, 181, 191]:
#     print('测试成功!')
# else:
#     print('测试失败!')

def action(n):
    return lambda x: x+n


# a = action(3)
# # print(type(a))
# # b = a(33)
# # print(type(b))
# # print(b)

# print(action(3)(33))
"""假设我们用一组tuple表示学生名字和成绩：

L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]

请用sorted()对上述列表分别按名字排序："""


L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
# def by_name(t):
#     return t[0]
#
#
# L2 = sorted(L, key=by_name)
# print(L2)
# print(L[0])


"""利用闭包返回一个计数器函数，每次调用它返回递增整数"""


def createCounter():
    f = [0]
    def counter():
        f[0] = f[0] + 1
        return f[0]
    return counter


# 测试:
counterA = createCounter()
print(counterA(), counterA(), counterA(), counterA(), counterA()) # 1 2 3 4 5
counterB = createCounter()
if [counterB(), counterB(), counterB(), counterB()] == [1, 2, 3, 4]:
    print('测试通过!')
else:
    print('测试失败!')