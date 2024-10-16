employees_count = int(input())

employees = dict()
namesakes_count = 0
namesakes_exist = False

for _ in range(employees_count):
    surname = input()
    employees[surname] = employees.get(surname, 0) + 1

employees = dict(sorted(employees.items()))

for surname, count in employees.items():
    if count > 1:
        print(f'{surname} - {count}')
        namesakes_exist = True

if not namesakes_exist:
    print('Однофамильцев нет')
