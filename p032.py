a=str(input())
for x in range (0,len(a)):
    print(a[:(x+1)])
for x in range (len(a)-1,-1,-1):
    print(a[:(x+1)])