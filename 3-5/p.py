from sys import stdin

query = input()

files = [file.strip() for file in stdin]

found = False

for filename in files:
    with open(filename, encoding='utf-8') as file:
        description = ' '.join(file.read().replace('&nbsp;', '').lower().split())

        if query.lower() in description:
            print(filename)
            found = True

if not found:
    print('404. Not Found')
