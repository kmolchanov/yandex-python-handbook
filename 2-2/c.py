petya_speed, vasya_speed, tolya_speed = int(input()), int(input()), int(input())

max_speed = max(petya_speed, vasya_speed, tolya_speed)

if max_speed == petya_speed:
    print('Петя')
elif max_speed == vasya_speed:
    print('Вася')
else:
    print('Толя')
