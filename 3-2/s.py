toys = []
unique = []

for _ in range(int(input())):
    name, toys_set = input().split(': ')
    toys.extend(set(toys_set.split(', ')))

for i in range(len(toys)):
    toy = toys.pop(0)
    if toy not in toys:
        unique.append(toy)
    toys.append(toy)

print('\n'.join(sorted(unique)))