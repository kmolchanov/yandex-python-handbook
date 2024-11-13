sum = 0

with open('numbers.num', 'rb') as file:
    while (chunk := file.read(2)):
        sum += int.from_bytes(chunk)

print(sum % 0x10000)
