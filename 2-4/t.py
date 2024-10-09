number = int(input())

max_sum = 0
best_base = 0

for base in range(10, 1, -1):
    temp_sum = 0
    temp_number = number
    while temp_number > 0:
        temp_sum += temp_number % base
        temp_number //= base
    if max_sum <= temp_sum:
        max_sum = temp_sum
        best_base = base

print(best_base)
