a,b,c=[int(i) for i in input().split()]
if a*a==b*b+c*c or b*b==a*a+c*c or c*c==a*a+b*b:
    print("yes")
else: print("no")