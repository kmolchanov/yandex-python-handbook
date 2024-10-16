employees_count = int(input())

employees = dict()
namesakes_count = 0

for _ in range(employees_count):
    surname = input()
    employees[surname] = employees.get(surname, 0) + 1

for surname, count in employees.items():
    if count > 1:
        namesakes_count += count

print(namesakes_count)
