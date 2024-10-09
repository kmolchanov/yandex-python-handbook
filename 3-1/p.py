length, lines_count = int(input()), int(input())
text = []

for _ in range(lines_count):
    text.append(input())

for line in text:
    if length > 3:
        print(line[:length - 3] + "..." if len(line) >= length - 3 else (line + "..." if length == 4 else line))
        length -= len(line)
