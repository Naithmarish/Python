x = int(input())
m = 1
while x > 0:
    y = x % 10
    m = m * y
    x = x // 10

print(m)