a,b,c=[int(i) for i in input().split()]
ans=1
for x in range(a,b+1):
    ans*=x
    ans%=c
print(ans)