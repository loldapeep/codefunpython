n = int(input())
x = []
y = []
if n < 3:
    print("CO")
else:
    a,b = [int(i) for i in input().split()]
    x.append(a)
    y.append(b)
    for j in range(2,n):
        if  ((x[j] - x[j - 1]) * (y[j - 1] - y[j - 2]) !=
	      (y[j] - y[j - 1]) * (x[j - 1] - x[j - 2])):
            print("KHONG")
            break
        if j == n - 1:
            print("CO")
            break
#rte
#not accepted