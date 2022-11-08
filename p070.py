a,b=[int(i) for i in input().split()]
ans = a%b
for x in range (0,69):
    ans *= 10
    ans %= b
ans *= 10
print(ans//b)