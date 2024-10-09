number = int(input())

original_number = number
reversed_number = 0

while number > 0:
    temp = number % 10
    reversed_number = reversed_number * 10 + temp
    number //= 10

print('YES') if reversed_number == original_number else print('NO')
