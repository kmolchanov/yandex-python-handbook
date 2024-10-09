string_numbers = input().split()

numbers = []

for number in string_numbers:
    numbers.append(int(number))

divisor = numbers[0]

for number in numbers[1:]:
    while divisor != 0 and number != 0:
        if divisor >= number:
            divisor -= number
        else:
            number -= divisor
    divisor = divisor + number

print(divisor)
