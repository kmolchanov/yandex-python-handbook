def make_equation(*coefficients):
    if len(coefficients) == 1:
        return f'{coefficients[0]}'
    else:
        return f'({make_equation(*coefficients[:-1])}) * x + {coefficients[-1]}'
