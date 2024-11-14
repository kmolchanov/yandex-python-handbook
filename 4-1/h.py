def is_palindrome(data):
    if isinstance(data, int):
        data = str(data)

    return data == data[::-1]
