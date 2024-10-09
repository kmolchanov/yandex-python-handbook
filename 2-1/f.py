product = str(input())
price = int(input())
weight = int(input())
payment = int(input())

sum = price * weight
change = payment - sum

print('Чек', f'{product} - {weight}кг - {price}руб/кг', sep='\n')
print(f'Итого: {sum}руб')
print(f'Внесено: {payment}руб')
print(f'Сдача: {change}руб')
