a, b, x, y, z = [float(d) for d in input().split()]
assert 0 < a or b or x or y or z < 10

if a > x and b > y or a > x and b > z or a > y and b > x or a > y and b > z or a > z and b > x or a > z and b > y:
    print('1')
else:
    print('0')
