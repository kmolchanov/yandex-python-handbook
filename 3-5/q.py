message = ''

with open('secret.txt', encoding='UTF-8') as file:
    data = file.read()
    for symbol in data:
        code = ord(symbol)
        if code < 128:
            message += chr(code)
        else:
            message += chr(code % 256)

print(message)
