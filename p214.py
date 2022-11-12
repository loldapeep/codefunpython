import sys
a,b=[int(i) for i in input().split()]
s=str(input())
count=0
for x in range (1,a):
    if s[x] == 'H':
        count+=1
    else: count=0
    if count>b-1:
        print("R. I. P")
        sys.exit()
print("YOLO!")