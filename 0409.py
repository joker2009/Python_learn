__author__ = 'Joker'
"""请定义一个函数quadratic(a, b, c)，接收3个参数，返回一元二次方程：

ax2 + bx + c = 0

的两个解。"""


def quadratic(a, b, c):
    if not isinstance(a, (int, float)):
        raise TypeError('参数类型错误')
    if not isinstance(b, (int, float)):
        raise TypeError('参数类型错误')
    if not isinstance(c, (int, float)):
        raise TypeError('参数类型错误')
    A = b * b - 4 * a * c
    if a == 0:
        if b == 0:
            if c == 0:
                return '方程根为全体实数'
            else:
                return '方程无根'
