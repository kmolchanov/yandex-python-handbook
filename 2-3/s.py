begin, end = 1, 1001

ask = (begin + end) // 2
print(ask)

while (x := input()) != 'Угадал!':
    if x == 'Меньше':
        end = (begin + end) // 2
    elif x == 'Больше':
        begin = (begin + end) // 2
    ask = (begin + end) // 2
    print(ask)
