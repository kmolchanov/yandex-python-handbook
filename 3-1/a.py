n = int(input())

success = True

for _ in range(n):
    word = input()
    if word[0] not in 'абв':
        success = False

print('YES') if success else print('NO')
