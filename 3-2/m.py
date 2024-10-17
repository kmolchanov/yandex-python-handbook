dishes_count = int(input())

dishes = set()

for _ in range(dishes_count):
    dish = input()
    if dish not in dishes:
        dishes.add(dish)

for _ in range(int(input())):
    for _ in range(int(input())):
        if (dish := input()) in dishes:
            dishes.remove(dish)

dishes = sorted(dishes)

if not dishes:
    print('Готовить нечего')
else:
    for dish in dishes:
        print(dish)
