import math
def isn(n):
	if ((n % 4 == 0 and n % 100 != 0) or n % 400 == 0) :
		return 1
	else:
		return 0
def dem (n):
    c=0
    d=0
    for i in range(2,n+1):
        for j in range (2, math.floor(math.sqrt(i))+1):
            c = 0
            if (i % j == 0):
                c+=1
                break
        if (c==0):
            d+=1
    return d
x,y,z=[int(i) for i in input().split()]
if (y==1): s = dem(x)
if (y==2): s = dem(x) + 11
if (y==3): s = dem(x) + 20
if (y==4): s = dem(x) + 31
if (y==5): s = dem(x) + 41
if (y==6): s = dem(x) + 52
if (y==7): s = dem(x) + 62
if (y==8): s = dem(x) + 73
if (y==9): s = dem(x) + 84
if (y==10): s = dem(x) + 94
if (y==11): s = dem(x) + 105
if (y==12): s = dem(x) + 115
if (isn(z) == 1 and y > 2): s+=1
print(s)