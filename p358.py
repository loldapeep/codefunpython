import math
n=int(input())
x=[]
y=[]
for i in range (0,n):
    a,b=[float(i) for i in input().split()]
    x.append(a); y.append(b)
sum=0
for i in range (1,n):
    sum+=math.sqrt((x[i]-x[i-1])**2+(y[i]-y[i-1])**2)
print ("{:.6f}".format(sum))
#not accepted
#full rte