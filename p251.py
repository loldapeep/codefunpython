sentence=0
word=1
s=str(input())
for x in range (0,len(s)):
    if s[x]=="." or s[x]=="!" or s[x]=="?": sentence+=1
    if s[x]==' ': word+=1
print(word, sentence)