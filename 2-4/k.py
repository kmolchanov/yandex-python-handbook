n = int(input())

simple_numbers_count = 0

for _ in range(n):
    number = int(input())
    is_simple, i = True, 2
    if number > 1:
        while i <= number ** 0.5 and is_simple:
            if number % i == 0:
                is_simple = False
            i += 1
    else:
        is_simple = False
    if is_simple:
        simple_numbers_count += 1

print(simple_numbers_count)
