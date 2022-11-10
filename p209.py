import sys
n=int(input())
a=[int(i) for i in input().split()]
b=0
for x in range (0, n):
    b+=a[x]
    if(b<0):
        print(f'DEFEATED AT CITY {x+1}')
        sys.exit()
print("VICTORY")
    