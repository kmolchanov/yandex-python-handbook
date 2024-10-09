product = str(input())
price = int(input())
weight = int(input())
payment = int(input())

sum = price * weight
change = payment - sum

delimiter = '='

price_to_print = f'{weight}кг * {price}руб/кг'
sum_to_print = f'{sum}руб'
payment_to_print = f'{payment}руб'
change_to_print = f'{change}руб'

print(f'{delimiter * 16}Чек{delimiter*16}')
print(f'Товар: {product:>28}')
print(f'Цена: {price_to_print:>29}')
print(f'Итого: {sum_to_print:>28}')
print(f'Внесено: {payment_to_print:>26}')
print(f'Сдача: {change_to_print:>28}')
print(f'{delimiter * 35}')
