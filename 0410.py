__author__ = 'Joker'


def fact(n):
    if n == 1:
        return 1
    return n * fact(n-1)

a = fact(5)
print(a)


def fact_2(n):
    return fact_iter(n, 1)


def fact_iter(num, product):
    if num == 1:
        return product
    return fact_iter(num-1, num*product)
# 汉诺塔 移动
# 每次讲N-1个盘子当做整体移动
"""迭代，把每一步递归例如 move(n-1,a,c,b) move(1,a,b,c) move(n-1,b,a,c) 再回代入move(n,a,b,c) 第二次时第一条公式就成 move(n-2,a,b,c) move(1,a,c,b) move(n-2,c,a,b)"""
def move(n, a,b,c):
    if n == 1:
        print(a, "-->", c)
    else:
        move(n-1, a, c, b)
        move(1, a, b, c)
        move(n-1, b, a, c)
move(3,"A","B","C")

"""奥义：不要去关心每一步怎么解决，只需要把函数当做一个工具，随时调用。也就是递归
1.我们给了一个move的工具，随时调用。只需要给他几个参数，就可以自动完成一个功能：
   就是把n个盘子利用跳板，将他从起点运送到终点，这个过程是严格遵守汉罗塔规则的

move(n,起点，跳板，终点)
现在有个n个盘子，a,b,c三个塔。

2.现在有个n个盘子，a,b,c三个塔。
把n个盘子抽象成两个盘子，n-1 和 底下最大的1

n = (n-1)+1
然后实现最简单的玩法

step1: 把n-1个盘子移动到跳板
step2: 把1个盘子移动到终点
step3: 把跳板上的n-1个盘子移动到终点
3.如何实现

move(n-1,a,c,b)
move(n,起点，跳板，终点)
一定要记住这个工具的样子

step1: move(n-1,a,c,b)
step2: move(1,a,b,c)
step3: move(n-1,b,a,c)
干！ 这工具如何结束，止不住？

step4<br>

if(n == 1):
    a -> c"""