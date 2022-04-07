n = int(input())
assert n <= 10**9
m = 1
while n > 2 ** m :
    m += 1
    print(2**(m - 1 ), end = ' ')

