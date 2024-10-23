from itertools import chain

purchases = [input().split(', ') for _ in range(3)]

purchases = sorted(set((chain.from_iterable(purchases))))

for i, v in enumerate(purchases, 1):
    print(f'{i}. {v}')
