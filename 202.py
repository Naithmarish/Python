x = int(input())
assert -1000 <= x <= 1000

if x >= 13:
    y = 3 * x**3 + 4 * x**2 + 5 * x + 6

elif x < 13:
    y = 3 * x**3 - 2 * x**2 - 3 * x - 4

print(y)