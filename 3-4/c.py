from itertools import count

start, end, step = [float(param) for param in input().split()]

for value in count(start, step):
    if value <= end:
        print(f'{value:.2f}')
    else:
        break
