transliteration_dictionary = {
    'А': 'A', 'Б': 'B', 'В': 'V', 'Г': 'G', 'Д': 'D', 'Е': 'E', 'Ё': 'E',
    'Ж': 'ZH', 'З': 'Z', 'И': 'I', 'Й': 'I', 'К': 'K', 'Л': 'L', 'М': 'M',
    'Н': 'N', 'О': 'O', 'П': 'P', 'Р': 'R', 'С': 'S', 'Т': 'T', 'У': 'U',
    'Ф': 'F', 'Х': 'KH', 'Ц': 'TC', 'Ч': 'CH', 'Ш': 'SH', 'Щ': 'SHCH',
    'Ы': 'Y', 'Э': 'E', 'Ю': 'IU', 'Я': 'IA', 'Ь': '', 'Ъ': ''
}

message, transliteration = '', ''

with open('cyrillic.txt', encoding='UTF-8') as cyrillic_file:
    for line in cyrillic_file:
        message += line

for symbol in message:
    if symbol.isupper():
        transliteration += transliteration_dictionary.get(symbol, symbol).capitalize()
    else:
        transliteration += transliteration_dictionary.get(symbol.upper(), symbol).lower()

with open('transliteration.txt', 'w', encoding='UTF-8') as transliteration_file:
    print(transliteration, file=transliteration_file)
