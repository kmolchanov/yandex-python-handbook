from itertools import permutations

n = int(input())

players = [input() for _ in range(n)]

commands = sorted(permutations(players))

for command in commands:
    print(', '.join(command))
