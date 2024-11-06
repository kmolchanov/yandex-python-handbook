filename = input()

with open(filename, encoding='UTF-8') as file:
    numbers = [int(number) for number in file.read().split()]

print(len(numbers))
print(len([number for number in numbers if number > 0]))
print(min(numbers))
print(max(numbers))
print(sum(numbers))
print(round(sum(numbers) / len(numbers), 2))
