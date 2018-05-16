"""计算素数的一个方法是埃氏筛法，它的算法理解起来非常简单"""


def _odd_iter():
    n = 3
    while True:
        yield n
        n = n + 2
        # yield n


# for i in _odd_iter():
#     print(i)
# print(type(_odd_iter()))


def _not_div(n):
    t = lambda x: x % n > 0
    return t

def prime():
    yield 2
    it = _odd_iter()
    while True:
        n = it.__next__()
        # print("n :" + str(n) )
        yield n
        it = filter(_not_div(n), it)
        # print(it)

    # while True:
    #     n = next(_odd_iter())
    #     print("n :" + str(n) )
    #     yield n
    #     it = filter(_not_div(n), _odd_iter())
    #
#
# for n in prime():
#     if n < 1000:
#         print(n)
#     else:
#         break


if __name__ == '__main__':
    for n in prime():
        if n < 1000:
            print(n)
        else:
            break
