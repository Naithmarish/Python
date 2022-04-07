x, y = [float(d) for d in input().split()]
h=2*x**2 - 4*x*y + 3*y**2 + (x+y)/7
print("{:.3f}".format(h))