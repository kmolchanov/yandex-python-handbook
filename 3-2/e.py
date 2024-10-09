n, m = int(input()), int(input())

semolina, oatmeal = set(), set()

for _ in range(n + m):
    eater = input()
    if eater in semolina:
        oatmeal.add(eater)
    else:
        semolina.add(eater)

eaters = semolina.symmetric_difference(oatmeal)

eaters_count = len(eaters)

print(eaters_count) if eaters_count > 0 else print('Таких нет')
