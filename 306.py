n = int(input())
t = abs(n)
m = 0
while n > 0:
    d = n % 10
    m = m * 10 + d
    n = n // 10

if m == t:
    print('Yes')
else:
    print('No')