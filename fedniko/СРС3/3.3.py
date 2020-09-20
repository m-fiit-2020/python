a = 'Hello world\nabcxyz\nabcdef\nthis is test\noh god of the north'
a = a.splitlines()

for i in range(len(a)):
    if a[i].startswith('abc') or a[i].endswith('yz') or a[i].find('no') != -1:
        print(a[i])


