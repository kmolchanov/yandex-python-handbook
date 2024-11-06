from sys import stdin

data = [word for word in stdin.read().split()]

words = set(data)

result = [word for word in words if word.lower() == word.lower()[::-1]]

print('\n'.join(sorted(result)))
