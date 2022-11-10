import math
def check(n):
    if round(math.sqrt(n))**2==n:
        return 1
    else: return 0
print(check(int(input())))