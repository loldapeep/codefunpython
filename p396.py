n=int(input())
t=0
a=[]; b=[]
for i in range (0,n):
    x,y=[int(i) for i in input().split()]
    a.append(x), b.append(y)
for i in range (0,n-1):
    for j in range (i+1,n):
        if a[i]==a[j] and b[i]==b[j]: t+=1
print(t)
#tle
#not accepted