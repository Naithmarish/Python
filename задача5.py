n = int(input())
assert 1 <= n <= 6
s = 0
if n == 1:
    for i in range(100, 1000):
        a = i // 100
        b = i // 10 % 10
        c = i % 10
        if a % 2 == 0 and b % 2 == 0 and c % 2 == 0:
            s +=i

    print(s)

elif n == 2:
    for i in range(100, 1000):
        a = i // 100
        b = i // 10 % 10
        c = i % 10
        if a < b < c:
            s +=1
    print(s)

elif n == 3:
    for i in range(100, 1000):
        a = i // 100
        b = i // 10 % 10
        c = i % 10
        if a % 2 == 1 and b % 2 == 1 and c % 2 == 1:
            s +=i
    print(s)

elif n == 4:
    for i in range(100, 1000):
        a = i // 100
        b = i // 10 % 10
        c = i % 10
        if a > b > c:
            s+=1
    print(s)

elif n == 5:
    for i in range(100, 1000):
        a = i // 100
        b = i // 10 % 10
        c = i % 10
        if i == a ** 3 + b ** 3 + c ** 3:
            s +=i
    print(s)

elif n == 6:
    for i in range(100, 1000):
        a = i // 100
        b = i // 10 % 10
        c = i % 10
        if a!= b and b != c and a != c:
            s +=1
    print(s)
