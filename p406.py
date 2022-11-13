a, b, x, y = [int(i) for i in input().split()]
import math
if a == 0:
    print("{:.2f}".format(abs(y-b)))
else:
    a1 = (-1)/a
    b1 = y - a1*x
    x1 = (b-b1)/(a1-a)
    y1 = a*x1+b
    print("{:.2f}".format(math.sqrt((x-x1)*(x-x1)+(y-y1)*(y-y1))))