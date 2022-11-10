def display(n):
    for x in range (0,n+1):
        print(("*")*(x*2+1))
    for x in range (n-1,-1,-1):
        print(("*")*(x*2+1))
display(int(input()))