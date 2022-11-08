import sys
a=int(input())
arr=[int(i) for i in input().split()]
sum=0
tempsum=0
for x in range (0,a):
    sum+=arr[x]
for x in range (sum,0,-1):
    if sum%x==0:
        for y in range (0,a):
            tempsum+=arr[y]
            if tempsum>(sum/x):
                break
            else:
                if tempsum==(sum/x):
                    tempsum=0
                    if y<x-1:
                        continue
                else: 
                    continue
            print(x)
            sys.exit()
    tempsum=0

