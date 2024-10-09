descriptions_count = int(input())
result_count = 0

for _ in range(descriptions_count):
    description = input()
    result_count = result_count + 1 if 'зайка' in description else result_count

print(result_count)
