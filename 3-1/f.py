n = int(input())

count = 0

for _ in range(n):
    description = input()
    count += description.count('зайка')

print(count)
