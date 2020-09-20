t = []

for i in [2] + list(range(3, 1000, 2)):
    if all(i % k != 0 for k in range(3, int(i**.5) + 1, 2)):
        t.append(i)

print(t)
