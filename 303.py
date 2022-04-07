n = int(input())
assert 0 <= n <= 2 * 10**9
m = 0
if n == 0:
    m = n + 1
else:
    pass

while (n > 0):
    n = n // 10
    m = m + 1


print(m)




