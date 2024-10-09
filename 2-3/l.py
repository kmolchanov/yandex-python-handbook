number = int(input())

max = 0

while number > 0:
    if max < number % 10:
        max = number % 10
    number //= 10

print(max)
