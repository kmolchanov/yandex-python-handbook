word = input()

word = word.replace(' ', '').lower()

comparison_word = ''

for i in range(len(word)):
    comparison_word += word[~i]

print('YES' if comparison_word == word else 'NO')
