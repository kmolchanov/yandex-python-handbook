sights = dict()

while (description := input()) != '':
    items = description.split()
    for item in items:
        if item not in sights:
            sights[item] = 1
        else:
            sights[item] += 1

for item in sights:
    print(item, sights[item])
