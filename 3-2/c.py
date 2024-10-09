descriptions_count = int(input())

items = set()

for _ in range(descriptions_count):
    description = input()
    items = items.union(set(description.split()))

for item in items:
    print(item)
