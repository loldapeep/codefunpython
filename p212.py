import sys
n,m,k=[int(i) for i in input().split()]
if n<0 or n>=10000 or m<0 or m>100 or k<0 or k>100:
    sys.exit()
for  x in range (0,k):
    n=n+(n*m/100)
print(round(n))