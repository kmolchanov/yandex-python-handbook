number = int(input())

result = ''

while number > 0:
    temp = number % 10
    number //= 10
    if temp % 2 != 0:
        result = str(temp) + result

print(result)
