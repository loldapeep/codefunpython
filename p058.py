def factor(n):
    s=""
    if n%2==0:
        s+=str(n//2)+" "+str(n//2)
    else:
        s+=str(n//2)+" "+str(n//2+1)
    return s
print(factor(int(input())))