x = int(input())
y = int(input())

a = x % 10
b = y % 10

c = x // 10 % 10
d = y // 10 % 10

e = x // 100 % 10
f = y // 100 % 10

g = (a + b) % 10
h = (c + d) % 10
i = (e + f) % 10

print(i, h, g, sep='')
