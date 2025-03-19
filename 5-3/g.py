class CyrillicError(Exception):
    pass


class CapitalError(Exception):
    pass


def name_validation(name) -> str:
    valid_cyrillic_chars = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
    if not isinstance(name, str):
        raise TypeError
    if not all([char.lower() in valid_cyrillic_chars for char in name]):
        raise CyrillicError
    if not name.istitle():
        raise CapitalError
    return name
