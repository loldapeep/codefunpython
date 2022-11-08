a,b,c=[int(i) for i in input().split()]
if a+b+c>=15:
    if a>=5 and b>=5 and c>=5:
        print("Excellent")
    else: print("Medium")
else: print("Fail")