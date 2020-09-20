n = int(input())
t = []
fact = []
j = 0

for i in [2] + list(range(3, 1000, 2)):
    if all(i % k != 0 for k in range(3, int(i**.5) + 1, 2)):
        t.append(i)
        
while n != 1:
    if n%t[j] == 0:
        n /= t[j]
        fact.append(t[j])
    else:
        j += 1
print(fact)
    
