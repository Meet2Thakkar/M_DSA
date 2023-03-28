a = []
for i in range(1,101):
    a.append(i)

for s in range(0,len(a)):
    if (a[s] % 3 == 0 and a[s] % 5 == 0):
        print("FizzBuzz")
    elif (a[s] % 3 == 0):
        print("Fizz")
    elif (a[s] % 5 == 0):
        print("Buzz")  
    else:
        print(a[s])