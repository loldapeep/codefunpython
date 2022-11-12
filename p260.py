import sys
c=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','0','1','2','3','4','5','6','7','8','9']
s=str(input())
cap=0
low=0
num=0
for x in range (0,len(s)):
    try:
        temp=int(s[x])
        num=1
        break
    except:
        pass
if s!=s.lower():
    cap=1
if s!=s.upper():
    low=1
if cap*low*num==0:
    print("Not perfect")
else: print("Perfect")