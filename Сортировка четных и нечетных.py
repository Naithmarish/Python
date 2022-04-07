input()
a = [int(d) for d in input().split()]
b = []
c = []
for i in range(0, len(a)):
    if a[i] % 2 == 0:
        b.append(a[i])
    else:
        c.append(a[i])

b.sort(reverse=True)
c.sort()
a = c + b
print(*a)