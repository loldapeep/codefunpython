import math
import sys
def check(n):
    for i in range(1, round(math.sqrt(n)) + 1):
        if (i**2 == n):
            return True
    return False
for x in range (int(input()), -1, -1):
    if(check(x)):
        print(int(math.sqrt(x)))
        sys.exit()