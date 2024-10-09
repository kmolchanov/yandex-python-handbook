count = int(input())

result_number = ''

for _ in range(count):
    number = int(input())
    max_number = 0
    temp = 0
    while number > 0:
        temp = number % 10
        number //= 10
        if temp > max_number:
            max_number = temp
    result_number += str(max_number)

print(result_number)
