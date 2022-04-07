n = int(input())
list = []
s = 2

while n > 1:
    if n % s == 0:
        list.append(s)
        n = n // s
    else:
        s += 1
print(list)
