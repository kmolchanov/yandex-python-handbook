numbers = sorted(map(int, input().split('; ')))
result = dict.fromkeys(numbers)

for i in numbers:
    for j in numbers:
        a, b = i, j
        while b:
            a, b = b, a % b
        if a == 1:
            if result[i]:
                result[i].add(j)
            else:
                result[i] = {j}

for number in result:
    if result[number]:
        print(f'{number} - {', '.join(map(str, sorted(result[number])))}')
