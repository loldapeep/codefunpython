import math
n=int(input())
a=[]
for x in range (n, 0, -1):
    if(n%x==0):
        a.append(x)
minval=100000
for x in range (1,len(a)):
    minval=min(minval,abs(a[x]-a[x-1]))
print(minval)
