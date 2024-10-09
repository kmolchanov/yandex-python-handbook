n = int(input())

pages = []

for _ in range(n):
    page = input()
    pages.append(page)

search_query = input()

for page in pages:
    if search_query.lower() in page.lower():
        print(page)
