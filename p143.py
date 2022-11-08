f=[0,0]
a=[int(i) for i in input().split()]
for x in range (0,5):
    if(a[x]%2==0):
        f[0]+=1
    else: f[1]+=1
if f[0]==4 or f[1]==4:
    print(1)
else: print(0)