total_weight = int(input())
total_price = int(input())
price_1 = int(input())
price_2 = int(input())

weight_1 = int((total_price - price_2) * total_weight / (price_1 - price_2))
weight_2 = int(total_weight - weight_1)

print(weight_1, weight_2)
