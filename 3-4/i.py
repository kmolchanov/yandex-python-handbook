from itertools import product, islice

n = int(input())

numbers = range(1, n + 1)

table = [x * y for x, y in product(numbers, repeat=2)]

start, end = 0, n

for i in range(n):
    print(*islice(table, start, end))
    start += n
    end += n
