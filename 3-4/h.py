from itertools import cycle, islice

m = int(input())

dishes = [input() for _ in range(m)]

n = int(input())

print('\n'.join(islice(cycle(dishes), n)))
