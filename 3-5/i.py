first, second = input(), input()

formated = []

with open(first, encoding='UTF-8') as first_file:
    for string in first_file:
        formated.append(string.strip().replace('\t', '').split())

formated = [item for item in formated if any(item)]

with open(second, 'w', encoding='UTF-8') as second_file:
    for string in formated:
        print(' '.join(string), file=second_file)
