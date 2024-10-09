x, y = 0, 0

while (direction := input()) != 'СТОП':
    steps = int(input())

    match direction:
        case 'СЕВЕР':
            y += steps
        case 'ЮГ':
            y -= steps
        case 'ЗАПАД':
            x -= steps
        case 'ВОСТОК':
            x += steps

print(y, x, sep='\n')
