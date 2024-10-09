a, b, c = int(input()), int(input()), int(input())

min = min(a, b, c)
max = max(a, b, c)

if min == a and max == b or min == b and max == a:
    mid = c
elif min == b and max == c or min == c and max == b:
    mid = a
else:
    mid = b

print('YES') if max < mid + min else print('NO')
