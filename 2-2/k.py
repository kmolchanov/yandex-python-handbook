number = input()

a = int(number[0])
b = int(number[1])
c = int(number[2])

min = min(a, b, c)
max = max(a, b, c)

if min == a and max == b or min == b and max == a:
    mid = c
elif min == b and max == c or min == c and max == b:
    mid = a
else:
    mid = b

print('YES') if mid * 2 == min + max else print('NO')
