a = 'In the hole in the ground there lived a hobbit'
b = a.partition('h')
c = a.rpartition('h')
print(b[0] + c[2])

