import math
a,b,c=[int(i) for i in input().split()]
t=b*b-4*a*c
if a==0:
    if b==0 and c==0: print("Inf")
    elif b==0 and c!=0: print("NO")
    elif b!=0 and c!=0: print('{:.2f}'.format(-c/b))
    elif b!=0 and c==0: print("0.00")
else:
    if t>0:
        if a>0:
            print('{:.2f}'.format((-b - math.sqrt(t))/(2*a)), '{:.2f}'.format((-b + math.sqrt(t))/(2*a)))
        else: print('{:.2f}'.format((-b + math.sqrt(t))/(2*a)), '{:.2f}'.format((-b - math.sqrt(t))/(2*a)))
    elif t==0: print('{:.2f}'.format(-b/(2*a)))
    else: print("NO")


