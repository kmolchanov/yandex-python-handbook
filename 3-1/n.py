string_numbers = input()
p = int(input())

numbers = string_numbers.split()

for number in numbers:
    print(int(number) ** p, end=' ')
