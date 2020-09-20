a = 'coffee'
k = 0
for i in range(len(a)):
    if a[i] == 'f':
        k += 1
    if k == 2:
        print(i)
        break
if k == 1:
    print(-1)
elif k == 0:
    print(-2)
