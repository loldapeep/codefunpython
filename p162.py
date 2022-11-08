a,b,c,t=[int(i) for i in input().split()]
if a==0 and b==0 and c==0 and t==0:
    print(0)
else:
    count=0
    for x in range (0,101):
        for y in range (0,101):
            for z in range (0,101):
                if(a*x+b*y+c*z==t): count+=1
    print(count)
#not accepted
#rte