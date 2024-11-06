first, second, answer = input(), input(), input()

with open(first, encoding='UTF-8') as first_file, open(second, encoding='UTF-8') as second_file:
    data1 = set([item for item in first_file.read().split()])
    data2 = set([item for item in second_file.read().split()])

with open(answer, 'w', encoding='UTF-8') as answer_file:
    diff = [item for item in data1 ^ data2]
    print(*sorted(diff), file=answer_file, sep='\n')
