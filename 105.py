x1, y1, x2, y2, x3, y3 = [float(d) for d in input().split()]
from math import sqrt

a=sqrt((x2-x1)**2 + (y2-y1)**2)
b=sqrt((x3-x2)**2 + (y3-y2)**2)
c=sqrt((x1-x3)**2 + (y1-y3)**2)

d=a+b+c

p=d/2
s=sqrt(p*(p-a)*(p-b)*(p-c))

print("{:.4f} {:.4f}".format(d, s))