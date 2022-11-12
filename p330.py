def choose(k, n):
    if 0 <= k <= n:
        ntok = 1
        ktok = 1
        for t in range(1, min(k, n - k) + 1):
            ntok *= n
            ktok *= t
            n -= 1
        return ntok // ktok
    else:
        return 0
inp = []
while True:
    try:
        line = list(map(int, input().split()))
        inp = inp + line
    except EOFError:
        break

n,m,u,v=[int(i) for i in inp.split()]
print(choose(n,m)-choose(n-2,m-2))
#not accepted
#rte