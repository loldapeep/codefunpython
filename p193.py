s=str(input())
count = [0]*4
for x in range (0,len(s)-1):
    if s[x]=="a":
        count[0]+=1
    elif s[x]=="b":
        count[1]+=1
    elif s[x]=="c":
        count[2]+=1
    else: count[3]+=1
for x in range (0,4):
    print(count[x])