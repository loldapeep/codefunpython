n,x,y=[int(i) for i in input().split()]
m=n*n
if m%2==0: print(m//2)
else:
    if (x+y)%2==0: print(m//2+1)
    else: print(m//2)