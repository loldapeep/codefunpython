n,m=[int(i) for i in input().split()]
a=[int(i) for i in input().split()]
sum=0
for x in range (0,n):
    sum+=a[x]
if sum%m==0: print(abs(sum)//m)
else:
    print(abs(sum)//m+1)
