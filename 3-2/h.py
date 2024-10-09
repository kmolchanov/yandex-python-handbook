n = int(input())

eaters = dict()

for i in range(n):
    info = input().split()
    eaters[info[0]] = info[1:]

porridge = input()

fans = list()

for name in eaters:
    if porridge in eaters[name]:
        fans.append(name)

if not fans:
    print('Таких нет')
else:
    fans.sort()
    for name in fans:
        print(name)
