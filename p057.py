import math
def count(n):
    cnt=0
    for x in range(1,round(math.sqrt(n))+1):
        if n%x==0:
            cnt+=1
    return cnt
print(count(int(input())))