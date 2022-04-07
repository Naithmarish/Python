n = int(input())
count = 0

for i in range(1, 10):
    while i % 10 % 2 == 1:
        count += 1
        i //= 10

print(count * 5 ** (n - 1))

