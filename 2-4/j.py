number = int(input())

print('А Б В')

for i in range(1, number):
    for j in range(1, number - i):
        print(f'{i} {j} {number - i - j}')
