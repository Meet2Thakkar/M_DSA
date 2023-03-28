X = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
n = 3
i = 1

p = int(n/2)
q = int(n-1)
X[p][q] = i
print(X)
print(p,q,i)
i += 1

p = p - 1
q = q + 1
if (p == -1):
    p = p - 1
elif (q == n):
    q = 0
X[p][q] = i
print(X)
print(p,q,i)
i += 1

p = p - 1
q = q + 1
if (p == -1):
    p = n - 1
elif (q == n):
    q = 0
X[p][q] = i
print(X)
print(p,q,i)
i += 1

p = p - 1
q = q + 1
if (X[p][q] != 0):
    p = p + 1
    q = q - 2
elif (p == -1):
    p = n - 1
elif (q == n):
    q = 0
X[p][q] = i
print(X)
print(p,q,i)
i += 1

p = p - 1
q = q + 1
if (X[p][q] != 0):
    p = p + 1
    q = q - 2
elif (p == -1):
    p = n - 1
elif (q == n):
    q = 0
X[p][q] = i
print(X)
print(p,q,i)
i += 1

p = p - 1
q = q + 1
if (X[p][q] != 0):
    p = p + 1
    q = q - 2
elif (p == -1):
    p = n - 1
elif (q == n):
    q = 0
X[p][q] = i
print(X)
print(p,q,i)
i += 1

p = p - 1
q = q + 1
if (p == -1 and q == n):
    p = 0
    q = n - 2
elif (X[p][q] != 0):
    p = p + 1
    q = q - 2
elif (p == -1):
    p = n - 1
elif (q == n):
    q = 0
X[p][q] = i
print(X)
print(p,q,i)
i += 1

p = p - 1
q = q + 1
if (p == -1 and q == n):
    p = 0
    q = n - 2
elif (X[p][q] != 0):
    p = p + 1
    q = q - 2
elif (p == -1):
    p = n - 1
elif (q == n):
    q = 0
X[p][q] = i
print(X)
print(p,q,i)
i += 1

# actual algo for magic square
p = p - 1
q = q + 1
print(p,q)
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

X[p][q] = i
print(X)
print(p,q,i)
i += 1