s = input()
count = 0
res = " "
prevc = " "

for c in s:
    if c != prevc:
        res += c
    prevc = c
for d in res[1:]:
    if d in '+-*/%':
        count += 1

print(count)