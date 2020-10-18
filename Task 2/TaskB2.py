lst=[1, 2, 2, 2, 1, 45, 5, 6, 6]

#lst = list(map(int, input().split()))

for i in lst:
    if i not in s:
        s.append(i)
print(s)
