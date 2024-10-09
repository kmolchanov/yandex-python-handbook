line = input()
data = line.split()
stack = [data[0]]

while data != []:
    symbol = data.pop(0)
    if symbol.isdigit():
        stack.append(int(symbol))
    else:
        match symbol:
            case '+':
                stack.append(stack.pop() + stack.pop())
            case '-':
                stack.append(stack.pop(-2) - stack.pop())
            case '/':
                stack.append(stack.pop(-2) / stack.pop())
            case '*':
                stack.append(stack.pop() * stack.pop())

print(stack[-1])
