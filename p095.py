n=int(input())
x=0
a=[0] * 100
for i in range (1,n//2+1):
    t=i
    s=0
    while s<n:
        s+=i
        i+=1
    if s==n:
        a[x]=t
        x+=1
    i = t
    if x>18:
        break
if a[0]==1 or x<11:
    j = a[0]
    s=0
    while s!=n:
        print(j,end=" ")
        s+=j
        j+=1
elif x==11:
    j = a[1]
    s=0
    while s!=n:
        print(j,end=" ")
        s+=j
        j+=1
else:
    j = a[18]
    s=0
    while s!=n:
        print(j,end=" ")
        s+=j
        j+=1
#not accepted