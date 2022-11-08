def alg(n):
    if n==0:
        return 2
    else: return alg(n-1)*2-1
print(alg(int(input()))**2)