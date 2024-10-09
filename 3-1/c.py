l, n = int(input()), int(input())

for _ in range(n):
    title = input()
    short_title = title[:l - 3].ljust(l, '.') if len(title) > l else title
    print(short_title)
