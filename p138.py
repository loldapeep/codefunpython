import sys
a=[int(i) for i in input().split()]*2
count=1
a.sort()
prev=0
for x in range (0,6):
    if a[x]==prev:
        count+=1
    else:
        count=1
    prev=a[x]
    if count==4:
        for y in range (x-3,6):
            a[y]=a[y+4]
        if a[0]==a[1]:
            print("Elephant")
        else: print("Bear")
        sys.exit()
print("Alien")