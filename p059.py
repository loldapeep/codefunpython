import math
import sys
a=int(input())
for x in range (round(math.sqrt(a)), 0, -1):
    if a%x==0:
        print(x, end=" ")
        print(a//x, end=" ")
        sys.exit()
