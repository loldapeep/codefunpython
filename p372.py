n,k=[int(i) for i in input().split()]
if n%2==0:
    if k<=n/2: print(2*k-1)
    else: print(2*k-n)
if n%2==1:
    if k<=(n+1)/2: print(2*k-1)
    else: print(2*k-n-1)