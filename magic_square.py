import numpy as np

n = int(input("N = "))
X = np.zeros((n,n))
i = 1

p = int(n/2)
q = int(n-1)
X[p][q] = i

for j in range(2,(n**2 + 1)):
    p = p - 1
    q = q + 1
    if (p == -1 and q == n):
        p = 0
        q = n - 2
    elif (p == -1):
        p = n - 1
    elif (q == n):
        q = 0
    elif (X[p][q] != 0):
        p = p + 1
        q = q - 2

    X[p][q] = j
print(X)