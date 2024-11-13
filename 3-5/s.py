chars = 'abcdefghijklmnopqrstuvwxyz'

shift = int(input()) % len(chars)

shifted_chars = chars[shift:] + chars[:shift]

alphabet = {key: value for key, value in zip(chars, shifted_chars)}
output = ''

with open('public.txt', encoding='UTF-8') as file:
    data = file.read()

    for char in data:
        new_char = alphabet[char.lower()] if char.lower() in alphabet else char
        output += new_char.upper() if char.isupper() else new_char

with open('private.txt', 'w', encoding='UTF-8') as file:
    file.write(output)
