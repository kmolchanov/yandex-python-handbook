from itertools import accumulate

string = input().split()

for result in accumulate([word + ' ' for word in string]):
    print(result)
