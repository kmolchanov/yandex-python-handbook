seen = set()

while description := input().split():
    for i, item in enumerate(description):
        if item == 'зайка' and i not in (0, len(description) - 1):
            seen.add(description[i - 1])
            seen.add(description[i + 1])
        elif item == 'зайка' and not i:
            seen.add(description[i + 1])
        elif item == 'зайка' and i == len(description) - 1:
            seen.add(description[i - 1])

for item in seen:
    print(item)
