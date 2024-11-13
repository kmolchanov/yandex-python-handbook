from sys import stdin
import json

json_name = 'scoring.json'

with open(json_name) as file:
    data = json.load(file)

answers = stdin.readlines()

score = 0

for tests in data:
    multiplier = int(tests['points'] / len(tests['tests']))
    for test in tests['tests']:
        result = test['pattern']
        for answer in answers:
            if result == answer.strip('\n'):
                score += multiplier

print(score)
