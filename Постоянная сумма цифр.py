n = int(input())
assert 0 <= n <=9
count = 0
for i in range(10, 100):
    i1 = i // 10
    i2 = i % 10
    s = i1 + i2

    d = i * n
    d1 = d // 100
    d2 = d // 10 % 10
    d3 = d % 10
    s1 = d1 + d2 + d3

    if s == s1:
        count += 1
print(count, end = " ")
