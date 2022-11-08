f=[0]*101
n=int(input())
a=[int(i) for i in input().split()]
b=[int(i) for i in input().split()]
for x in range (1,a[0]+1):
    f[a[x]]=1
for x in range (1,b[0]+1):
    f[b[x]]=1
sum=0
for x in range (1,n+1):
    sum+=f[x]
if sum==n:
    print("WIN")
else: print("LOSE")