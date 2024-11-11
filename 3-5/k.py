import json

filename_input, filename_output = input(), input()

with open(filename_input, encoding='UTF-8') as file:
    numbers = [int(number) for number in file.read().split()]

statistics = {
    'count': len(numbers),
    'positive_count': len([number for number in numbers if number > 0]),
    'min': min(numbers),
    'max': max(numbers),
    'sum': sum(numbers),
    'average': round(sum(numbers) / len(numbers), 2),
}

with open(filename_output, 'w', encoding='UTF-8') as file:
    json.dump(statistics, file, ensure_ascii=False, indent=4)
