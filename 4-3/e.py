def result_accumulator(func):
    data = []

    def wrapper(*args, method='accumulate'):
        data.append(func(*args))

        if method == 'drop':
            result = data.copy()
            data.clear()

            return result

    return wrapper
