number = int(input())

is_simple, i = True, 2

if number > 1:
    while i <= number ** 0.5 and is_simple:
        if number % i == 0:
            is_simple = False
        i += 1
else:
    is_simple = False

result = 'YES' if is_simple else 'NO'

print(result)
