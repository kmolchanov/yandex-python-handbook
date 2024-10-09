a, b, c = int(input()), int(input()), int(input())

min = min(a, b, c)
max = max(a, b, c)

if min == a and max == b or min == b and max == a:
    mid = c
elif min == b and max == c or min == c and max == b:
    mid = a
else:
    mid = b
hypotenuse = max ** 2
cathetus_sum = mid ** 2 + min ** 2

if hypotenuse > cathetus_sum:
    print('велика')
elif hypotenuse < cathetus_sum:
    print('крайне мала')
else:
    print('100%')
