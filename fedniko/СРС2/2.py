z = [1, 2, 3, 2, 4, 5, 6, 6, 7, 8, 7, 20, 20]
a = z
i = 0

while i < len(a):
    if a.count(a[i]) > 1:
        a.remove(a[i])
    i += 1
print(a)

# z = [1, 2, 3, 2, 4, 5, 6, 6, 7, 8, 7, 20, 20]
# n = []
#
# for i in z:
#     if i not in n:
#         n.append(i)
#
# print(n)

# def f(l):
#     n = []
#     for i in l:
#         if i not in n:
#             n.append(i)
#     return n
#
#
# print f([1, 1, 2, 3, 3, [4, 5, 6]]) # [1, 2, 3, [4, 5, 6]]
# print f([[1, 2], [1, 2], 3, 4, 4, 'oops', 'oops']) # [[1, 2], 3, 4, 'oops']
