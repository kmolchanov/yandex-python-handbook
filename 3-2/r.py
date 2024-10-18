treasures = {}

for _ in range(int(input())):
    x, y = input().split()
    index = (int(x) // 10, int(y) // 10)
    treasures[index] = treasures.get(index, 0) + 1

print(max(treasures.values()))