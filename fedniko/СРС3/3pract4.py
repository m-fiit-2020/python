a = 'Hello world\nabcxyz\nabcdef\nthis is test'
a = a.splitlines()

i = 0
for i in range(len(a)):
    if a[i].startswith('abc'):
        print(a[i])


