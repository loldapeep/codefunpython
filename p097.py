import sys
k=int(input())
s=str(input())
if k >= len(s):
    print(0)
    sys.exit()
else:
    for x in range (0,k):
        i=1
        while i<len(s) and ord(s[i-1])>=ord(s[i]):
            i+=1
        if i!=len(s):
            s=s[:(i-1)]+s[i:]
        else:
            s=s[:(i-1)]
print(s)
#not accepted