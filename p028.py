a,b=[int(i) for i in input().split()]
s=0
for x in range (1,a+1):
    s+=x*(x+b)
print (s)