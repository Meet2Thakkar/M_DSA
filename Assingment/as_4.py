L = [1, 54, 56, 44, 39, 86, 97, 1, 13, 73, 31, 5, 95, 74, 88]
p = []

for i in range(len(L)):
    if (L[i] % 2 != 0):
        p.append(L[i])
p.sort()
L.sort()
print(p)
print(L)
print(len(p))
print(len(L))