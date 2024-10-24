from sys import stdin

changes = [int(data.split()[2]) - int(data.split()[1]) for data in stdin.readlines()]

average = round(sum(changes) / len(changes))

print(average)
