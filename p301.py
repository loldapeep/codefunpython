n,k=[int(i) for i in input().split()]
a=[int(i) for i in input().split()]
b=[]
for x in range (0,n):
    if(a[x]%k==0):
        b.append(a[x])
for x in range (0,len(b)):
    print(b[x],end=' ')