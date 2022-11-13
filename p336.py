k,n=[int(i) for i in input().split()]
def C(len,last):
    sum=0
    if len==k: return 1
    if len>k: return 0
    if last>n: return 0
    for x in range (last, n+1):
        sum+=C(len+1,x)
    return sum
print(C(0,1))