a ,b, c, d, f = [float(z) for z in input().split()]
from math import sqrt
P1 = a + b + f
S1 = sqrt(P1/2 * (P1/2 - a) * (P1/2 - b) * (P1/2 - f))

P2 = c + d + f
S2 = sqrt(P2/2 * (P2/2 - c) * (P2/2 - d) * (P2/2 - f))

S = S1 + S2

print("{:.4f}".format(S))