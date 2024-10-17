numbers = input().split()

result = []

for number in numbers:
    binary_number = bin(int(number))[2:]
    info = {
        "digits": len(binary_number),
        "units": binary_number.count('1'),
        "zeros": binary_number.count('0'),
    }
    result.append(info)

print(result)
