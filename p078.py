k=int(input())
a=[int(i) for i in input().split()]
count=0
def digit(n):
    if n==0:
        return 1
    else:
        i=0
        while 10**i<=n:
            i+=1
        return i
def sum(n):
    ans = 0
    b = digit(n)
    for x in range (b, -1, -1):
        a = n//(10**x)
        ans += a
        n -= a*(10**x)
    return ans
def check(n):
    if n%sum(n)==0:
        return True
    else:
        return False
for x in range(0,len(a)):
    if check(a[x]):
        count+=1
print(count)