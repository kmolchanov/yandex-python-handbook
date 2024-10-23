from itertools import permutations

n = int(input())

players = [input() for _ in range(n)]

commands = sorted(permutations(players, 3))

for command in commands:
    print(', '.join(command))
