import os
# os.name
print(os.name)
"""利用Python的特性来过滤文件。比如我们要列出当前目录下的所有目录，只需要一行代码："""
# [x for x in os.listdir('.') if os.path.isdir(x)]
"""要列出所有的.py文件，也只需一行代码"""
x= [x for x in os.listdir('.') if os.path.isfile(x) and os.path.splitext(x)[1] == '.py']
for i in x:
    print(i)

"""
利用os模块编写一个能实现dir -l输出的程序。
编写一个程序，能在当前目录以及当前目录的所有子目录下查找文件名包含指定字符串的文件，并打印出相对路径。
"""



