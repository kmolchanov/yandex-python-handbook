n, m = int(input()), int(input())

cell_size = len(str(n * m))

number = 1
for _ in range(n):
    for _ in range(m):
        print(f'{number:>{cell_size}}', end=' ')
        number += 1
    print()
