S1, R1 = [float(d) for d in input().split()]
from math import pi
from math import sqrt
S = pi * R1 ** 2
S2 = S - S1
R2 = sqrt(S2 / pi)

print("{:.2f}".format(R2))