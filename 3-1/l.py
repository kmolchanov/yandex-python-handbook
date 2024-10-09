n = int(input())

menu = ['Манная', 'Гречневая', 'Пшённая', 'Овсяная', 'Рисовая']

for i in range(n):
    print(menu[i % len(menu)])
