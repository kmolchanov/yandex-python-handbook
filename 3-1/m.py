n = int(input())

numbers = []

for _ in range(n):
    number = int(input())
    numbers.append(number)

p = int(input())

for number in numbers:
    print(number ** p)
