a,b=[float(i) for i in input().split()]
n=a**b
if int(a)==float(a): print(int(n))
else: print("{:.2f}".format(n))
#not accepted
#float precision