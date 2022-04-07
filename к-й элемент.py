n, k = (int(d) for d in input().split())
a = [int(f) for f in input().split()]
a.insert(0, 0)
for g in range(1, len(a)-1):
    for i in range(1, len(a)-1):
        if a[i] > a[i+1]:
            a[i], a[i+1] = a[i+1], a[i]
        else:
            pass
        if a[1] > a[2]:
            a[1], a[2] = a[2], a[1]
        else:
            pass
    print(*a)
print(*a)
print(a[k])