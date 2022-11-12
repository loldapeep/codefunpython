s=str(input())
s=list(s)
n=int(input())
for x in range (0,n):
    a,b=[int(i)-1 for i in input().split()]
    if a>=len(s) or b>=len(s): continue
    temp=s[a]
    s[a]=s[b]
    s[b]=temp
print(''.join(s))
#not accepted
#20(rte)