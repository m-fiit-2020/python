n = 24
i = 2
factor = []
while i * i <= n:
    if n % i == 0:
        factor.append(i)
        n = n / i
        n = int(n)
    else:
        i = i + 1
factor.append(n)
print(factor)
