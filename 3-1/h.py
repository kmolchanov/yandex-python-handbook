n = int(input())

for _ in range(n):
    description = input()
    position = description.find('зайка') + 1
    if position > 0:
        print(position)
    else:
        print('Заек нет =(')
