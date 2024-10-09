n, m = int(input()), int(input())

cell_size = len(str(n * m))

for i in range(n):
    for j in range(m):
        if j % 2 == 0:
            number = j * n + i + 1
        else:
            number = (j + 1) * n - i
        print(f'{number:>{cell_size}}', end=' ')
    print()
