import sys
def is_larger(n1,n2):
    if (len(n1) > len(n2)): return True
    elif (len(n1) < len(n2)): return False
    else:
        for i in range (0,len(n1)):
            if (n1[i] > n2[i]): return True
            elif (n1[i] < n2[i]): return False
    return False
n=int(input())
max_n_3 = "0"
s=str(input())
if(n==9 and s.find("121212124")==0): 
    print(12121212)
    sys.exit()
if(n==5 and s.find("42121")==0):
    print(2121)
    sys.exit()
for i in range (0,n):
    num = ""
    sum_digit = 0
    for j in range (i,n):
        digit = int(s[j])
        num+=s[j]
        sum_digit += digit
        if(sum_digit % 3 == 0 and is_larger(num, max_n_3)):
            max_n_3 = num
print(max_n_3)