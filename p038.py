import math
def digit(n):
    i=0
    while 10**i<n:
        i+=1
    return i
a,b=[float(i) for i in input().split()]
c=round(a, 7-digit(a))
print(c)
d=round(b, 7-digit(b))
c*=a
c=round(c, 7-digit(c))
print(c)
c*=a
c=round(c, 7-digit(c))
print(c)
print(d)
d*=b
d=round(d, 7-digit(d))
print(d)
d*=b
d=round(d, 7-digit(d))
print(d)
print("{:.2f}".format(c+d))
#not accepted