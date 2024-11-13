import json
from sys import stdin

filename = input()

with open(filename, encoding='UTF-8') as file:
    data = json.load(file)

additional_data = [item for item in stdin.read().split('\n') if any(item)]

for additional_item in additional_data:
    key, value = additional_item.split('==')
    data[key.strip()] = value.strip()

with open(filename, 'w', encoding='UTF-8') as file:
    json.dump(data, file, sort_keys=False, indent=4, ensure_ascii=False)
