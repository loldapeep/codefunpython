a,b,c=[int(i) for i in input().split()]
d,e,f=[int(i) for i in input().split()]
if c<f: print(1)
elif c>f: print(2)
else:
    if b<e: print(1)
    elif b>e: print(2)
    else:
        if a<d: print(1)
        else: print(2)
