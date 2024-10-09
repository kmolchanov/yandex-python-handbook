password = input()

a = int(password[0]) + int(password[1])
b = int(password[1]) + int(password[2])

if a > b:
    print(a, b, sep='')
else:
    print(b, a, sep='')
