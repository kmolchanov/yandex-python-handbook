common_string = ''
letter = ''
frequency = 0

while (string := input()) != "ФИНИШ":
    common_string += string.lower().replace(' ', '')

for i in common_string:
    count = common_string.count(i)
    if count > frequency:
        frequency = count
        letter = i
    elif count == frequency:
        if i < letter:
            letter = i

print(letter)
