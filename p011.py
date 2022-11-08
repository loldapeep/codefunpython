import math
a,b,c=input().split()
a=int(a)
b=int(b)
c=int(c)
p=(a+b+c)/2
print("{:.6f}".format(round(math.sqrt(p*(p-a)*(p-b)*(p-c)),6)))