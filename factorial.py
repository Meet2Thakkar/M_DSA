num = int(input("num = "))
factorial = 1
if num < 0:
    print("Factorial does not exist")
elif num == 0:
    print("Factorial of 0 is 1")
else:
    for i in range(1,num+1):
        factorial = factorial*i
    print("Factorial of",num,"is ",factorial)

def fact(x):
    if x == 1:
        return 1
    else:
        return(x * fact(x-1))
        
print("factorial of", num, "is", fact(num))