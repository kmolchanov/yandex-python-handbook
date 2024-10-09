count = int(input())

total_sum = 0

for _ in range(count):
    number = int(input())
    sum = 0
    while number > 0:
        sum += number % 10
        number //= 10
    total_sum += sum

print(total_sum)
