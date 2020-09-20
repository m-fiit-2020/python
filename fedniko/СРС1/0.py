n = input('Введите n-ый член ряда Фибоначи: ')
n = int(n)
a = 1
b = 1
while n > 2:
    for i in range(2, n):
        c = a + b
        a = b
        b = c
    print(c)
    break
else:
    if n == 1:
        print(1)
    else:
        print(1)
