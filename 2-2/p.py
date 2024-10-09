petya_speed, vasya_speed, tolya_speed = int(input()), int(input()), int(input())

max_speed = max(petya_speed, vasya_speed, tolya_speed)
min_speed = min(petya_speed, vasya_speed, tolya_speed)

first = 'Петя'
second = 'Вася'
third = 'Толя'

if max_speed == petya_speed:
    first = 'Петя'
    if min_speed == vasya_speed:
        second = 'Толя'
        third = 'Вася'
    else:
        second = 'Вася'
        third = 'Толя'
elif max_speed == vasya_speed:
    first = 'Вася'
    if min_speed == petya_speed:
        second = 'Толя'
        third = 'Петя'
    else:
        second = 'Петя'
        third = 'Толя'
else:
    first = 'Толя'
    if min_speed == petya_speed:
        second = 'Вася'
        third = 'Петя'
    else:
        second = 'Петя'
        third = 'Вася'

print(f'{first: ^24}')
print(f'{second: ^8}{" ": ^16}')
print(f'{" ": ^16}{third: ^8}')
print(f'{"II": ^8}{"I": ^8}{"III": ^8}')
