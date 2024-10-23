from itertools import permutations

purchases = []

for _ in range(int(input())):
    purchases.extend(input().split(', '))

for item in sorted(permutations(purchases, 3)):
    print(*item)
