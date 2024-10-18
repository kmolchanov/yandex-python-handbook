friends = {}

while combination := input():
    person1, person2 = combination.split()
    friends[person1] = friends.get(person1, set()) | {person2}
    friends[person2] = friends.get(person2, set()) | {person1}

relations = dict.fromkeys(friends, set())

for person in friends:
    for friend in friends[person]:
        relations[person] = relations[person].union(friends[friend])
    relations[person].discard(person)
    for friend in friends[person]:
        relations[person].discard(friend)

result = []

for person in relations:
    result.append(f'{person}: {", ".join(sorted(relations[person]))}')

result.sort()

for item in result:
    print(item)
