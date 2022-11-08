import math
a,b,c = input().split()
a = float(a)
b = float(b)
c = float(c)
if a == 0:
    if b == 0:
        if c == 0:
            print("Inf")
        else:
            print("No solution")
    else:
        print("{:.2f}".format((-c/b)))
else:
    delta =  b*b-(4*a*c)
    if delta == 0:
        x = -b/(2*a)
        print("{:.2f}".format(x))
    elif delta > 0:
        x1=(-b+math.sqrt(delta))/(2*a)
        x2=(-b-math.sqrt(delta))/(2*a)
        if x1 < x2:
            print("{:.2f}".format(x1),"{:.2f}".format(x2))
        else:
            print("{:.2f}".format(x2),"{:.2f}".format(x1))
    else:
        print("No solution")
    