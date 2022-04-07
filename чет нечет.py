n = int(input())
assert 1 <= n <= 20
for x in range(1, n+1):
    x = int(input())
    if x % 2 == 0:
        print(x, 'is even')
    else:
        print(x, 'is odd')