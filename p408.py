n = int(input())
i = 1
f = 0
f1 = 1
f2 = 1
while f <= n:
    f = f1+f2
    f1 = f2
    f2 = f
    i += 1
print(i-2)