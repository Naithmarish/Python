n = int(input())
m = 0
p = 0
z = 0
while n > 0:
    d = n % 10
    m = m * 10 + d
    n //= 10
    z = z + (m % 10) * 2 ** (p + 1)
    m //= 10


print(z)