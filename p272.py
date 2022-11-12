n=int(input())
a=[int(i) for i in input().split()]
x,y=[int(i) for i in input().split()]
sum=0
for i in range (0,n):
    sum+=a[i]
e=min(x,y)
f=max(x,y)
tempsum=0
for i in range (e-1,f-1):
    tempsum+=a[i]
k=min(tempsum, sum-tempsum)
print(k)