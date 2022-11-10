n,m=[int(i) for i in input().split()]
bill=[int(i) for i in input().split()]
iCount = [0]*n
for i in range (0,n):
    if(m >= bill[i]):
        temp = m//bill[i]
        iCount[i] = temp
        m -= temp*bill[i]
for i in range (0,n):
    print(iCount[i])