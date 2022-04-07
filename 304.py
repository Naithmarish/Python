n = int(input())
assert n <= 2 * 10**9
s = 0
m = 1
while n > 0:
    s = s + n % 10
    m = m * (n % 10)
    n = n // 10
t = m / s
print("{:.3f}".format(t))
