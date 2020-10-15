def comb(n, k):
    if k==0 or n==k:
        return 1
    return comb(n-1, k) + comb(n-1, k-1)
n = int(input("Enter n: "))
k = int(input("Enter k: "))
print(comb(n, k))

