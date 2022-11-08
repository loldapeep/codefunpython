m,n=[int(i) for i in input().split()]
a=[str(i) for i in input().split()]
b=[str(i) for i in input().split()]
def display(ans):
    pos = 0
    while pos < len(ans):
        if pos+50<len(ans):
            print(ans[(pos):(pos+50)])
            pos+=50
        else:
            print(ans[(pos):])
            break
a1=''
b1=''
for x in range (0,m):
    a1+=a[x]
for x in range (0,n):
    b1+=b[x]
ans=int(a1)+int(b1)
ans=str(ans)
display(ans)
