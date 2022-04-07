n = int(input())
s = 0
a = 10 ** (n - 1)
b = a - (a / 10 * 2)
s = a + b
while True:
    b = b - b / 10
    if b.is_integer():
        s += b
    else:
        break
print(int(s))