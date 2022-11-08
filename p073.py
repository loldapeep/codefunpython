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
        return "YES"
    else:
        return "NO"
print(check(int(input())))