numbers_filename, even_filename, odd_filename, equal_filename = input(), input(), input(), input()

with open(numbers_filename, encoding='UTF-8') as file:
    strings = [string for string in file.read().split('\n') if any(string)]

even_symbols, odd_symbols = '02468', '13579'

evens_string, odds_string, equals_string = '', '', ''

for string in strings:
    evens, odds, equals = [], [], []

    for number in string.split():
        evens_count = odds_count = 0
        for symbol in number:
            if symbol in even_symbols:
                evens_count += 1
            elif symbol in odd_symbols:
                odds_count += 1

        if evens_count > odds_count:
            evens.append(number)
        elif odds_count > evens_count:
            odds.append(number)
        elif evens_count == odds_count:
            equals.append(number)

    evens_string += ' '.join(evens) + '\n'
    odds_string += ' '.join(odds) + '\n'
    equals_string += ' '.join(equals) + '\n'

with (open(even_filename, 'w', encoding='UTF-8') as even_file,
      open(odd_filename, 'w', encoding='UTF-8') as odd_file,
      open(equal_filename, 'w', encoding='UTF-8') as equal_file):
    even_file.write(evens_string)
    odd_file.write(odds_string)
    equal_file.write(equals_string)
