warehouse = int(input())
market = int(input())
speed = int(input())

distance = market - warehouse
delivery_time = distance / speed

print(f"{delivery_time:.2f}")
