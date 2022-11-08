import math
a,b,c = input().split()
a = float(a)
b = float(b)
c = float(c)
if a == 0:
    if b == 0:
        if c == 0:
            print("inf")
        else:
            print(0)
    else:
        print(1)
elif a==1 and b==0 and c==1:
    print(2)
else:
    delta =  b*b-(4*a*c)
    if delta == 0:
        x = -b/(2*a)
        print(1)
    elif delta > 0:
        x1=(-b+math.sqrt(delta))/(2*a)
        x2=(-b-math.sqrt(delta))/(2*a)
        if x1 < x2:
            print(2)
        else:
            print(2)
    else:
        print(0)
    