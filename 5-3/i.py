class CyrillicError(Exception):
    pass


class CapitalError(Exception):
    pass


class BadCharacterError(Exception):
    pass


class StartsWithDigitError(Exception):
    pass


def name_validation(name) -> str:
    valid_cyrillic_chars = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
    if not isinstance(name, str):
        raise TypeError
    if not all([char.lower() in valid_cyrillic_chars for char in name]):
        raise CyrillicError
    if name.capitalize() != name:
        raise CapitalError
    return name


def username_validation(username) -> str:
    valid_username_chars = 'abcdefghijklmnopqrstuvwxyz_0123456789'
    if not isinstance(username, str):
        raise TypeError
    if not all([char.lower() in valid_username_chars for char in username]):
        raise BadCharacterError
    if username[0].isdigit():
        raise StartsWithDigitError
    return username


def user_validation(*args, **kwargs) -> dict:
    allowed = ['last_name', 'first_name', 'username']
    user = kwargs

    try:
        if any([user[field] == '' for field in allowed]):
            raise KeyError
    except Exception:
        raise KeyError

    if not all([field in allowed for field in user.keys()]):
        raise KeyError

    name_validation(user['last_name'])
    name_validation(user['first_name'])
    username_validation(user['username'])

    return user
