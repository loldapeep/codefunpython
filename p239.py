d,x,g=[int(i) for i in input().split()]
s=str(input())
t=0
for i in range (0,len(s)):
    if s[i]=='r': 
        t+=g
    else: 
        e=t%(d+x)
        if e<=d: t+=(d-e)
        t+=g
print(int(t))
#not accepted 
#wa for some reason, will work fine in c++