from itertools import product

n, m = int(input()), int(input())

ln = len(str(n * m))

for i, j in product(range(1, n + 1), range(1, m + 1)):
    print(f'{((i - 1) * m + j):>{ln}}', end=' ')
    if j == m:
        print()
