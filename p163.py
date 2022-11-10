n = int(input())
a = [int(i) for i in input().split()]
dem = 0
res = 0
for i in range(0,n):
    if i == 0 or a[i] != a[i-1]:
        dem = 1
    else:
        dem = dem + 1
    if res < dem:
        res = dem

print(res) 
#not accepted
#same problem with p162