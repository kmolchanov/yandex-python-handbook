def answer(func):
    def result(*args, **kwargs):
        return f'Результат функции: {func(*args, **kwargs)}'
    return result
