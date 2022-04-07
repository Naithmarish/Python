input()
b = [int(x) for x in input().split()]
ass = b[-1]

for i in range(len(b)-1, 0, -1):
    b[i] = b[i - 1]
b[0] = ass

print(*b)
