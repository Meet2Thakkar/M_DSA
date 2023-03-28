# There is list L containing some numbers. Write a program to create a new list which contains the numbers which are either divisible by 5 or 7 or both. Print that new list in ascending order.

A =[61, 90, 81, 95, 49, 23, 89, 28, 86, 5]
P = []

for i in range(len(A)):
    if (A[i] % 5 == 0):
        P.append(A[i])
    elif (A[i] % 7 == 0):
        P.append(A[i])
    elif (A[i]%5==0 and A[i]%7==0):
        P.append(A[i])
print(P)

