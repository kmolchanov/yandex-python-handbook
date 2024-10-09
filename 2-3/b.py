count = 0

while (description := input()) != 'Приехали!':
    if 'зайка' in description:
        count += 1

print(count)
