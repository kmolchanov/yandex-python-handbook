number = int(input())

delay = 0

for i in range(1, number + 1):
    for j in range(3 + delay, 0, -1):
        print(f'До старта {j} секунд(ы)')
    print(f'Старт {i}!!!')
    delay += 1
