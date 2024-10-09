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

if min == 0:
    print(f'{mid}{min} {max}{mid}')
else:
    print(f'{min}{mid} {max}{mid}')
