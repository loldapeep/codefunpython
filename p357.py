import sys
a,b,c,d=[int(i) for i in input().split()]
try:
    x=(d-b)/(a-c)
except ZeroDivisionError:
    print("0.000000 0.000000")
    sys.exit()
y=a*x+b
print('{:.6f}'.format(x), '{:.6f}'.format(y))