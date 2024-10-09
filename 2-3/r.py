number = int(input())
divider = 1

if number < 2:
    print(number)
while number > 1:
    divider += 1
    if not number % divider:
        print(divider, end='')
        if number != divider:
            print(' *', end=' ')
        number //= divider
        divider = 1
