a,b,c=[float(i) for i in input().split()]
if a+b>c and b+c>a and a+c>b: print("NONDEGENERATE")
elif a+b==c or a+c==b or b+c==a: print("DEGENERATE")
else: print("IMPOSSIBLE")