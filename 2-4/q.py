n = int(input())

palindromes_count = 0

for _ in range(n):
    number = int(input())

    original_number = number
    reversed_number = 0

    while number > 0:
        temp = number % 10
        reversed_number = reversed_number * 10 + temp
        number //= 10

    if reversed_number == original_number:
        palindromes_count += 1

print(palindromes_count)
