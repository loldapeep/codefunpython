import math
s=[int(i) for i in input().split()]
n=s[0]
s.pop(0)
x=[]
y=[]
for i in range (0,n):
    x.append(s[2*i]); y.append(s[2*i+1])
sum=0
for i in range (0,n):
    sum+=math.sqrt((x[i]-x[i-1])**2+(y[i]-y[i-1])**2)
print(sum)


#not accepted
#rte