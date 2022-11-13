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
n,m=[int(i) for i in input().split()]
sum=0
for x in range (1, m+2-n):
    sum+=choose(x,m+1-n)
print(sum)