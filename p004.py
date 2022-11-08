import math
a=int(input())
b=math.floor((a-1)/2)+1
count=0
for x in range (b,a):
    count+=1
print(count)