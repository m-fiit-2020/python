def nod(a, b):
    if b == 0:
        return a
    return nod(b, a%b)
a = int(input("Enter a: "))
b = int(input("Enter b: "))
if a > b:
    print(nod(a,b))
else:
    print(nod(b,a))
        
