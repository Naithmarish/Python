a, b, c = [float(d) for d in input().split()]
if a > b > c or c > b > a:
    print("{:.0f}".format(b))

elif b > a > c or c > a > b:
    print("{:.0f}".format(a))

elif b > c > a or a > c > b:
    print("{:.0f}".format(c))
