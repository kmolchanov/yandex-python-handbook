number_1 = int(input())
number_2 = int(input())

a = number_1 // 10
b = number_1 % 10
c = number_2 // 10
d = number_2 % 10

min = min(a, b, c, d)
max = max(a, b, c, d)

sum = a + b + c + d

mid = (sum - min - max) % 10

print(f'{max}{mid}{min}')
