s=str(input())
c=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
count=0
for x in range (0,len(s)):
    if s[x].lower()==s[x] and s[x] in c:
        count+=1
print(count)
print(s.upper())