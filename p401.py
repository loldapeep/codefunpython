n = int(input())
cs = 1
m = n
while n >= 10:
    cs += 1
    n = n // 10
s = 0
for i in range(1,cs):
    s = s + 9 * i * pow(10,i-1)
t = (m - pow(10,cs - 1) + 1) * cs
print(s+t)