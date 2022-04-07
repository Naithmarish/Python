s = input()
res = " "
for c in s:
    if c in 'qwertyuiopasdfghjklzxcvbnm':
        c *= 2
    res += c

print(res)