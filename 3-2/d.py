n, m = int(input()), int(input())

semolina, oatmeal = set(), set()

for _ in range(n):
    semolina.add(input())

for _ in range(m):
    oatmeal.add(input())

omnivores = semolina.intersection(oatmeal)

print(len(omnivores)) if len(omnivores) > 0 else print('Таких нет')
