from itertools import combinations

n = int(input())

print('А Б В')

for i, j in list(combinations(range(1, n), 2)):
    print(i, j - i, n - j)
