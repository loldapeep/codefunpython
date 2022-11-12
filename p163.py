inp = []
while True:
    try:
        line = list(map(int, input().split()))
        inp = inp + line
    except EOFError:
        break

n = inp[0]
x = inp[-1]
inp.pop(0)
inp.pop(-1)

ans = 0
for i in inp:
    if i == x:
        ans = 1
print(ans)
#cre: Bùi Quang Nguyên