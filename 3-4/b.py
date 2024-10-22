command1, command2 = input(), input()

commands = zip(command1.split(', '), command2.split(', '))

for command in commands:
    print(f'{command[0]} - {command[1]}')
