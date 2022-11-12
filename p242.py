def checkint(n):
    try:
        temp=int(n)
        return True
    except:
        return False
s=str(input())
for x in range (0,len(s)):
    if not checkint(s[x]):
        print(s[x],end='')