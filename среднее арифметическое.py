input()
b = [float(x) for x in input().split()]
c = []
for i in b:
    if i > 0:
        c.append(i)
    else:
        pass
if len(c) > 0:
    print("{:.2f}".format(sum(c) / len(c)))
else:
    print('Not Found')

