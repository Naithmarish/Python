a, b, n = [float(d) for d in input().split()]
assert 0 <= a or b or n <= 100
cost = n * (100 * a + b)

print("{:.0f} {:.0f}".format(cost // 100, cost % 100))