count = int(input())

winner = ''
max_number = 0

for i in range(count):
    name = input()
    number = int(input())
    sum = 0
    while number > 0:
        sum += number % 10
        number //= 10
    if sum >= max_number:
        winner = name
        max_number = sum

print(winner)
