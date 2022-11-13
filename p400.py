n = int(input())
dem = 0
while True:
    if n > 5:
        n = n -5
        dem += 1
    else:
        dem += 1
        break
print(dem)