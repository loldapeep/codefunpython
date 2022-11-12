s=str(input())
for x in range (0,len(s)):
    if ord(s[x])>=97:
        print(1,end='')
    else: print(0,end='')