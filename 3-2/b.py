set_1 = set(input())
set_2 = set(input())

intersection_set = set_1.intersection(set_2)

for symbol in intersection_set:
    print(symbol, end='')
