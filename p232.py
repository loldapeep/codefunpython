n,m=[int(i) for i in input().split()]
c=[""]*1001
found=False
for x in range (0,n):
    a,b=(input().split())
    a=int(a); b=str(b)
    c[a]=b
for x in range (0,m):
    d=int(input())
    if(c[d]==""):
        print("Not found")
    else: print(c[d])
    