import sys
a,k=[int(i) for i in input().split()]
arr=[int(i) for i in input().split()]
sum=0
tempsum=0
for x in range (0,a):
    sum+=arr[x]
if sum%(k+1)!=0:
    print("NO")
    sys.exit()
for x in range (0,a):
    tempsum+=arr[x]
    if tempsum>(sum/(k+1)*k):
        print("NO")
        sys.exit()
    elif tempsum==sum/(k+1)*k:
        print(a-x-1,end=" ")
        print(x+1,end=" ")
        sys.exit()
    elif tempsum==sum/(k+1):
        print(x+1,end=" ")
        print(a-x-1,end=" ")
        sys.exit()

