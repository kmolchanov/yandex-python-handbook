total_sum = 0
discount = 0.10
discount_condition = 500

while (price := float(input())) != 0:
    if price >= discount_condition:
        total_sum += price - price * discount
    else:
        total_sum += price

print(total_sum)
