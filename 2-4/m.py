n, m = int(input()), int(input())

cell_size = len(str(n * m))

for i in range(n):
    number = i + 1
    for _ in range(m):
        print(f'{number:>{cell_size}}', end=' ')
        number += n
    print()
