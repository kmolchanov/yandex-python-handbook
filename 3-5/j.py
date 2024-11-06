filename, lines_count = input(), int(input())

with open(filename, encoding='UTF-8') as file:
    data = [item for item in file.read().split('\n') if any(item)]

print('\n'.join(data[-lines_count:]))
