description1 = input()
description2 = input()
description3 = input()

if description1 > description2:
    description1, description2 = description2, description1
if description1 > description3:
    description1, description3 = description3, description1
if description2 > description3:
    description2, description3 = description3, description2

if 'зайка' in description1:
    print(description1, len(description1))
elif 'зайка' in description2:
    print(description2, len(description2))
elif 'зайка' in description3:
    print(description3, len(description3))
