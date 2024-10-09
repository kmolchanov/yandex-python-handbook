n, m = int(input()), int(input())

cell_size = len(str(n * m))

for i in range(n):
    for j in range(m):
        if i % 2 == 0:
            number = i * m + j + 1
        else:
            number = (i + 1) * m - j
        print(f'{number:>{cell_size}}', end=' ')
    print()
