n = int(input())

fact = []

for i in [2] + list(range(3, int(n**.5) + 1, 2)):
    while n%i == 0:
        fact.append(i)
        n /= i
if n != 1:
    fact.append(int(n))

print(fact)
