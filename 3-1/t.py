expression = input()
tokens = expression.split()

uno = ['~', '#', '!']
duo = ['+', '-', '*', '/']
trio = ['@']
operators = uno + duo + trio

stack = []

while tokens != []:
    token = tokens.pop(0)
    if token in uno:
        a = stack.pop()
        match token:
            case '~':
                stack.append(-a)
            case '!':
                res = 1
                for i in range(1, a + 1):
                    res *= i
                stack.append(res)
            case '#':
                stack.append(a)
                stack.append(a)
    elif token in duo:
        a = stack.pop()
        b = stack.pop()
        match token:
            case '+':
                stack.append(b + a)
            case '-':
                stack.append(b - a)
            case '*':
                stack.append(b * a)
            case '/':
                stack.append(b // a)
    elif token in trio:
        a = stack.pop()
        b = stack.pop()
        c = stack.pop()
        match token:
            case '@':
                stack.append(b)
                stack.append(a)
                stack.append(c)
    else:
        stack.append(int(token))

print(int(stack[-1]))
