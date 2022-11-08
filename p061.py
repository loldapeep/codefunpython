n=int(input())
f=[0,1]
for x in range (2,n+1):
    f.append(f[x-1]+f[x-2])
print(f[n])