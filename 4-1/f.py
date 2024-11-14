result = []


def modern_print(message):
    print(message) if message not in result else None
    result.append(message)
