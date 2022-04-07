s = input()
s1 = []
s2 = []
word = ""
r = 0
for c in s:
    if c.isalnum():
        word += c.lower()
    elif word:
        s2.append(word)
        word = ""
if word:
    s2.append(word)

for d in s2:
    if d == d[::-1]:
        s1.append(d)
if s1:
    print(s2.index(max(s1, key=len)) + 1)

else:
    print('0')



