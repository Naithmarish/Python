count = 0
while True:
    n = int(input())
    if n == 0:
        break
    if n > 0:
        continue
        pass
    if n < 0:
        count += 1
        continue
print(count)
