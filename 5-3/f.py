class InfiniteSolutionsError(Exception):
    pass


class NoSolutionsError(Exception):
    pass


def find_roots(a, b, c):
    if not all(type(num) in (int, float) for num in (a, b, c)):
        raise TypeError

    if a == b == c == 0:
        raise InfiniteSolutionsError('Infinite solutions')
    elif a == 0 and b != 0 and c != 0:
        roots = (-(c / b), -(c / b))
    elif a == b == 0:
        raise NoSolutionsError('No solution')
    elif a == c == 0:
        roots = (0, 0)
    else:
        disc = (b ** 2) - (4 * a * c)
        if disc == 0:
            roots = ((-b) / (2 * a), (-b) / (2 * a))
        elif disc > 0:
            x1 = (-b - (disc ** 0.5)) / (2 * a)
            x2 = (-b + (disc ** 0.5)) / (2 * a)
            roots = tuple(sorted([x1, x2]))
        else:
            raise NoSolutionsError('No solution')
    return roots
