ingredients_count = int(input())

ingredients, dishes = [], set()

for _ in range(ingredients_count):
    ingredient = input()
    ingredients.append(ingredient)

for _ in range(int(input())):
    dish = input()
    dishes.add(dish)
    for _ in range(int(input())):
        if input() not in ingredients:
            dishes.discard(dish)

dishes = sorted(dishes)

if not dishes:
    print('Готовить нечего')
else:
    for dish in dishes:
        print(dish)
