number = int(input())

count = 0

for _ in range(number):
    is_summarized = False
    while (description := input()) != 'ВСЁ':
        if 'зайка' in description and not is_summarized:
            count += 1
            is_summarized = True

print(count)