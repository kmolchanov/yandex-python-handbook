from sys import stdin

for line in stdin.readlines():
    if (line.startswith('#')):
        continue
    else:
        print(line.split('#')[0].rstrip('\n'))
