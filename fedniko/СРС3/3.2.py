a = 'Hello world'
a = a.lower()
b = ''
for i in a:
    if i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u':
        b += i.upper()
    else:
        b += i
print(b)
