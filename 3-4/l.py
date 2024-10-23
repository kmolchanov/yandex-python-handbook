purchases = []

for _ in range(int(input())):
    purchases.extend(input().split(', '))

for i, v in enumerate(sorted(purchases), 1):
    print(f'{i}. {v}')
