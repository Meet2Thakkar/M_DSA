#x = input("A = ")
#y = input("B = ")
#sum = int(x) + int(y)
#print("The sum is: ", sum)

#x = input("A = ")
#y = input("B = ")
#z = input("C = ")

#if x > y:
#    if x > z:
#        print("A is greater")
#    else:
#        print("C is largest")
#else:
#    if y > z:
#        print("B is gretest")
#    else:
#        print("C is greatest")

import cmath as cm

a = int(input("X = "))
b = int(input("Y = "))
c = int(input("Z = "))

d = int(pow(b,2)) - int(4*a*c)

if d >= 0:
    r1 = ((-b + cm.sqrt(d))/2*a)
    r2 = ((-b - cm.sqrt(d))/2*a)
    print(f"r1 = {r1}, r2 = {r2}")
else:
    rp = (-b/2*a)
    ip = (cm.sqrt(d)/2*a)
    print(f"The solution are {rp} + {ip}")
