n=int(input())
f=[0,1]
x=1
while f[x]<=n:
    f.append(f[x]+f[x-1])
    x+=1
if f[x-1]==n:
    print("YES")
else:
    print("NO")