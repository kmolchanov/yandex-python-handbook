class BadCharacterError(Exception):
    pass


class StartsWithDigitError(Exception):
    pass


def username_validation(username) -> str:
    valid_username_chars = 'abcdefghijklmnopqrstuvwxyz_0123456789'
    if not isinstance(username, str):
        raise TypeError
    if not all([char.lower() in valid_username_chars for char in username]):
        raise BadCharacterError
    if username[0].isdigit():
        raise StartsWithDigitError
    return username
