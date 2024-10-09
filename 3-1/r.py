code = input()

current_symbol = code[0]
repetitions = 1

for symbol in code[1:]:
    if symbol == current_symbol:
        repetitions += 1
    else:
        print(current_symbol, repetitions)
        current_symbol = symbol
        repetitions = 1

print(current_symbol, repetitions)
