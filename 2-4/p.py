size, cell_size = int(input()), int(input())

delimiter = '-' * (size * cell_size + size - 1)

for i in range(1, size + 1):
    for j in range(1, size + 1):
        print(f'{i * j:^{cell_size}}', end='')
        if j < size:
            print('|', end='')
        else:
            print()
    if i < size:
        print(delimiter)
