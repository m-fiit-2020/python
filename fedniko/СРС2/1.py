z = 1000
for n in range(2, z):
    for x in range(2, n):
        if n % x == 0:
            break
    else:
        print(n)
