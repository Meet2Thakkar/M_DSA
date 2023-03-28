

L = [80, 19, 25, 55, 65, 27, 6, 47, 24, 50, 93, 37, 93, 91, 5, 93]
n = 2
P =[]

def rev(lis, num):
    sam = list(set(lis))
    sam.sort()
    return sam[-num:]

print(rev(L, n))