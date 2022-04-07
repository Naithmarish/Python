s = input()
s = s.lower()
exc = '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'
sol = []

for p in exc:
    if p in s:
        s = s.replace(p, "")

w = s.split()
wr = s[::-1].split()

wr_rev = list(reversed(wr))

for i in range(len(w)):
    if w[i] == wr_rev[i]:
        sol.append(w[i])

r = max(sol, key=len)
print(w.index(r) + 1)

