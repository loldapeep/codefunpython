def mod(m,n):
    if m*n<0:
        return m%n-n
    else: return m%n
a,b,c,d,e = [int(i) for i in input().split()]
print(mod((a+b)*(c+d),e))