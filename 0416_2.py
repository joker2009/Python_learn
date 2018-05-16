

def is_odd(n):
    return lambda n: n % 2 == 1


# L = list(filter(lambda x: x % 2 == 1, range(1, 20)))
# print(L)

L = list(filter(is_odd(1), range(1, 20)))
print(L)

# a = is_odd(3)
# print(a)


"""
上面的函数相当于一个闭包,下面调用的时候无法执行内部的lambda函数,所以运行结果还是原来的list
楼主这种写法lambda函数中的n是内部函数的局部变量，is_odd函数的形参n并未使用过
"""
