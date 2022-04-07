input()
b = [int(x) for x in input().split()]
c = []
for i in b:
    if i not in c:
        c.append(i)
print(*c)

