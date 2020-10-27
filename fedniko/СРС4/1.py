# Пытался выводить ключ по значению (Страна - ключ, город - значение)
# Потратил кучу времени, чтобы попытаться реализовать это (не получилось)
# Идея была записывать список в ключ
# n = int(input())
# my_dict = dict(input().split() for _ in range(n))
#
#
# k = int(input())
# for _ in range(k):
#     print(list(my_dict.keys())[list(my_dict.values()).index(input())])

# Понял, что можно город сделать ключом, а страну значением
# Это куда проще, так как в словаре не может быть одинаковых ключей, но могут быть одинаковые значения
n = int(input())
my_dict = {}
for _ in range(n):
    value, *keys = input().split()  # * - при вводе первое значение - это value, остальные keys
    for key in keys:
        my_dict[key] = value

k = int(input())
for _ in range(k):
    print(my_dict[input()])
