size = int(input())

line = 1
step = 1

max_length = 0

while step <= size:
    str_line = ''
    for i in range(line):
        if step > size:
            break
        str_line += str(step) + ' '
        step += 1
    if len(str_line) > max_length:
        max_length = len(str_line)
    line += 1

line = 1
step = 1

while step <= size:
    str_line = ''
    for i in range(line):
        if step > size:
            break
        str_line += str(step) + ' '
        step += 1
    print(f'{str_line:^{max_length}}', end=' ')
    print()
    line += 1
