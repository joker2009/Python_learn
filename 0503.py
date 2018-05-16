# def fab(max):
#     n, a, b = 0, 0, 1
#     # print(n)
#     while n < max:
#         # print(b)
#         yield a
#         a, b = b, a+b
#         n += 1
#
# a = fab(10)
# for i in a:
#     print(i)

def sort(lists):
    count = len(lists)
    for i in range(0, count):
        for j in range(i + 1, count):
            if lists[i] < lists[j]:
                lists[i], lists[j] = lists[j], lists[i]
    return lists


a = [1, 3, 4, 5, 0, 1]
b = sort(a)
print(b)
