def make_linear(data):
    result = []

    for item in data:
        if type(item) is list:
            result.extend(make_linear(item))
        else:
            result.append(item)

    return result
