def secret_replace(text, **replaces):
    result = ''

    for symbol in text:
        if symbol in replaces:
            result += replaces[symbol][0]
            replaces[symbol] = replaces[symbol][1:] + (replaces[symbol][0],)
        else:
            result += symbol

    return result
