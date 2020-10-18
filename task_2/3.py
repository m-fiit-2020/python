def factor(n):
    if n < 1 or n > 1000 or not isinstance(n, int):
        raise TypeError
    i = 2 
    answer = list()
    while n != 1:
        if n % i == 0:
            n = n // i
            answer.append(i)
            continue
        i += 1
    for i in answer:
        print(i, end = ' ')

n = int(input("Введите n: "))
factor(n)
