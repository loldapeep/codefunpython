a,b,c,n=[int(i) for i in input().split()]
for i in range (-abs(n)+1, abs(n)):
    for j in range (-abs(n)+1, abs(n)):
        if a*i*i+b*i+c==j:
            print(i,j, end=" ")