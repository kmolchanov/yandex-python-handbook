import hashlib


class MinLengthError(Exception):
    pass


class PossibleCharError(Exception):
    pass


class NeedCharError(Exception):
    pass


possible_password_chars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789'


def password_validation(password, min_length=8,
                        possible_chars=possible_password_chars,
                        at_least_one=str.isdigit) -> str:
    if not isinstance(password, str):
        raise TypeError
    if len(password) < min_length:
        raise MinLengthError
    if any([char not in possible_chars
            for char in password]):
        raise PossibleCharError
    if not any([at_least_one(char) for char in password]):
        raise NeedCharError

    hash_object = hashlib.sha256()
    hash_object.update(password.encode())
    hash = hash_object.hexdigest()

    return hash
