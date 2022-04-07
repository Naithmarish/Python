n = int(input())
assert 1 < n
for i in range(1, n +1):
    y = i ** 3
    if y < n:
        print(y, end=" ")
    else:
        break
