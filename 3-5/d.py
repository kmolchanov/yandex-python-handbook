from sys import stdin

pages = [line.strip('\n') for line in stdin.readlines()]
query = pages.pop()

results = [page for page in pages if query.lower() in page.lower()]

print(*results, sep='\n')
