"""面向对象编程"""

"""创建实例是通过类名+()实现的："""


class Student(object):
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def print_score(self):
        print('%s:%s' % (self.name, self.score))


a = Student('A', 23)
# b = Student('B', 27)

print(a.name, a.print_score())
# print(b.name, b.print_score())
