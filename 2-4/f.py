count = int(input())
divisor = int(input())

for _ in range(1, count):
    number = int(input())
    while divisor != 0 and number != 0:
        if divisor >= number:
            divisor -= number
        else:
            number -= divisor
    divisor = divisor + number

print(divisor)
