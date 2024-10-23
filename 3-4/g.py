from itertools import combinations

n = int(input())

players = [input() for _ in range(n)]

commands = list(combinations(players, 2))

for command in commands:
    print(f'{command[0]} - {command[1]}')
