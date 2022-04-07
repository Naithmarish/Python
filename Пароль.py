s = input().rstrip()
f = 0
g = 0
h = 0
j = 0
k = 0

for c in s:
    if 'a' <= c <= 'z':
        f = 1

    if 'A' <= c <= 'Z':
        g = 1

    if '0' <= c <= '9':
        h = 1

    if c in '!"#$%&/()*+':
        j = 1

if len(s) >= 8:
    k = 1

print(f + g + h + j + k)



