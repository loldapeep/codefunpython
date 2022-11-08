n=int(input())
f=[0,1]
x=1
while f[x]<=n:
    f.append(f[x]+f[x-1])
    x+=1
print(f[x-1])