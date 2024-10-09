k, n = int(input()), int(input())

if k > n:
    step = -1
else:
    step = 1

for i in range(k, n + step, step):
    print(i, end=' ')
