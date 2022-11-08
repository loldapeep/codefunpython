def check(n):
    if n%3==0 and n!=3:
        return "YES"
    else:
        return "NO"
print(check(int(input())))