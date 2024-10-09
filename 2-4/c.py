size = int(input())

line = 1
step = 1

while step <= size:
    for i in range(line):
        if step > size:
            break
        print(step, end=' ')
        step += 1
    print()
    line += 1
