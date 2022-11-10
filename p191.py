import sys
a=[int(i) for i in input().split()]
sum=0
for x in range (0,len(a)):
    sum+=a[x]
    if a[x]==0:
        print(sum)
        sys.exit()