x1,y1,x2,y2,x3,y3 = [int(i) for i in input().split()]
a = (y2-y1)/(x2-x1)
b = y1-a*x1
if a*x3+b==y3:
    print(1)
else:
    print(0)