s = input()
s = s.replace(' ', '')

if s == s[::-1]:
    print('YES')
else:
    print('NO')