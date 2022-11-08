a,b,c=input().split()
a=float(a); b=float(b); c=str(c)
def ans():
    if c=="+": return a+b
    if c=="-": return a-b
    if c=="*": return a*b
    if c=="/": return a/b
print("{:.2f}".format(ans()))

