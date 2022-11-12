n=int(input())
def calc(x):
    if x==n: return 1
    sum=0
    for i in range (x+1,n+1):
        sum+=calc(i)
    return sum
print(calc(1))