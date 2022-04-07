a, b, c, d = [int(n) for n in input().split()]
assert 1 <= a and b and c and d <= 10

if a >= b and c >= d:
    products = [False for m in range((a * c) + 1)]
    for i in range(a, b - 1, -1):
        for j in range(c, d - 1, -1):
            p = i * j
            products[p] = True

elif b >= a and d >= c:
    products = [False for m in range((b * d) + 1)]
    for i in range(a, b + 1):
        for j in range(c,d + 1):
            p = i * j
            products[p] = True

elif a >= b and d >= c:
    products = [False for m in range((a * d) + 1)]
    for i in range(a,b - 1, -1):
        for j in range(c,d + 1):
            p = i * j
            products[p] = True

elif b >= a and c >= d:
    products = [False for m in range((b * c) + 1)]
    for i in range(a, b + 1):
        for j in range(c,d - 1, -1):
            p = i * j
            products[p] = True

print(sum(products))
