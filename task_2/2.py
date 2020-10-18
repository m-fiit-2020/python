my_list = input("Введите массив чисел: ").split()
new_list = list()
for i in my_list:
    if i not in new_list:
        new_list.append(i)
print(new_list)
