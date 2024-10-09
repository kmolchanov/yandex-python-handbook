a, b = int(input()), int(input())

c = a * b

while a != 0 and b != 0:
    if a >= b:
        a -= b
    else:
        b -= a

print(c // (a + b))
