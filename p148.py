a,b=[int(i) for i in input().split()]
if a==0 or b==0: print("%")
else:
    if a%b==0 or b%a==0: print("%")
    else: print(0)