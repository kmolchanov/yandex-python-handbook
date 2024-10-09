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

if eaters_count > 0:
    for eater in sorted(eaters):
        print(eater)
else:
    print('Таких нет')