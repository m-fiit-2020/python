first = second = 1
n = int(input("Введите n-ый член ряда Фиббоначи: ")) - 2
while n > 0:
    first, second= second, first + second
    n -= 1
print(second)
