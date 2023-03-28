N = []
for i in range(int(input())):
    name = input()
    score = float(input())
    
    arr = [name, score]
    N.append(arr)
    
#sc = N[(N.index(min(N))) + 1]
N.sort(key = lambda x: x[1])
#sc = N[(N.index(min(N))) + 1]
print(N[0])