n=[int(i) for i in input().split()]
if n[1]%2==0: d=0
else: d=n[1]*n[1]
for x in range (2,n[0]+1):
    if n[x]%2==1: d+=n[x]*n[x]-n[x-1]*n[x-1]
s=d*3.141592654
print("{:.6f}".format(s))

