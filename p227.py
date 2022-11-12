s1=str(input())
s2=str(input())
count=0
for x in range (0,256):
    if chr(x) in s2 and chr(x) in s1:
        count+=1
print(count)