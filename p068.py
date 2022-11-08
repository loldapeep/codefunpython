dig = [1,1,2,6,4,2,2,4,2,8]
def ans(n):
    if n<10:
        return dig[int(n)]
    if ((n//10)%10)%2==0:
        return (6*ans(n/5)*dig[int(n%10)]) % 10
    else:
        return (4*ans(n/5)*dig[int(n%10)]) % 10
print(ans(int(input())))