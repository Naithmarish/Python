p = int(input())
array = []
a = [int(k) for k in input().split()]
b = [int(o) for o in input().split()]
n = int(input())

for i in range(p):
    array.extend(f for f in range(a[i], b[i] + 1))
array.sort()
print(array[n])