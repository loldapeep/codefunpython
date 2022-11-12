c=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',' ']
a=[0]*27
s=str(input()).lower()
for x in range (0, len(s)):
    a[c.index(s[x])]+=1
ans=1
for x in range (0,26):
    ans*=a[x]
if ans!=0:
    print("YES")
else: print("NO")