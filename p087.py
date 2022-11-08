n=int(input())
f=["","A","B"]
for x in range (3,n+1):
    f.append(f[x-1]+f[x-2])
print(f[n])