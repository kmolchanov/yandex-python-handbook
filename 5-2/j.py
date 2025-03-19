class Fraction():
    def __init__(self, *args):
        self.__den = 1
        if isinstance(args[0], str):
            splits = args[0].split('/')
            if len(splits) == 1:
                self.__num = int(args[0])
            else:
                self.__num, self.__den = [int(c) for c in splits]
        elif len(args) == 1 and isinstance(args[0], int):
            self.__num = args[0]
        else:
            self.__num = args[0]
            self.__den = args[1]
        self.__reduction()

    def __neg__(self):
        return Fraction(-self.__num, self.__den)

    def __check_other(self, other):
        if isinstance(other, int):
            return Fraction(other, 1)
        return other

    def __add__(self, other):
        other = self.__check_other(other)
        denominator = self.denominator() * other.denominator()
        numerator = self.__num * other.__den + other.__num * self.__den
        return Fraction(numerator, denominator)

    def __radd__(self, other):
        return self.__add__(other)

    def __iadd__(self, other):
        other = self.__check_other(other)
        self.__num = self.__num * other.__den + other.__num * self.__den
        self.__den = self.__den * other.__den
        self.__reduction()
        return self

    def __sub__(self, other):
        other = self.__check_other(other)
        denominator = self.denominator() * other.denominator()
        numerator = self.__num * other.__den - other.__num * self.__den
        return Fraction(numerator, denominator)

    def __rsub__(self, other):
        return -self.__sub__(other)

    def __isub__(self, other):
        other = self.__check_other(other)
        self.__num = self.__num * other.__den - other.__num * self.__den
        self.__den = self.__den * other.__den
        self.__reduction()
        return self

    def __mul__(self, other):
        other = self.__check_other(other)
        denominator = self.__den * other.__den
        numerator = self.__num * other.__num
        return Fraction(numerator, denominator)

    def __rmul__(self, other):
        return self.__mul__(other)

    def __imul__(self, other):
        other = self.__check_other(other)
        self.__num = self.__num * other.__num
        self.__den = self.__den * other.__den
        self.__reduction()
        return self

    def __truediv__(self, other):
        other = self.__check_other(other)
        new = Fraction(self.__num, self.__den)
        return new.__mul__(other.reverse())

    def __rtruediv__(self, other):
        return self.__truediv__(other).reverse()

    def __itruediv__(self, other):
        other = self.__check_other(other)
        return self.__imul__(other.reverse())

    def __gt__(self, other):
        other = self.__check_other(other)
        return self.__num * other.__den > other.__num * self.__den

    def __rgt__(self, other):
        return self.__gt__(other)

    def __lt__(self, other):
        other = self.__check_other(other)
        return self.__num * other.__den < other.__num * self.__den

    def __rlt__(self, other):
        return self.__lt__(other)

    def __ge__(self, other):
        other = self.__check_other(other)
        return self.__num * other.__den >= other.__num * self.__den

    def __rge__(self, other):
        return self.__ge__(other)

    def __le__(self, other):
        other = self.__check_other(other)
        return self.__num * other.__den <= other.__num * self.__den

    def __rle__(self, other):
        return self.__le__(other)

    def __eq__(self, other):
        other = self.__check_other(other)
        return self.__num * other.__den == other.__num * self.__den

    def __req__(self, other):
        return self.__eq__(other)

    def __ne__(self, other):
        other = self.__check_other(other)
        return self.__num * other.__den != other.__num * self.__den

    def __rne__(self, other):
        return self.__ne__(other)

    def __str__(self):
        return f'{self.__num}/{self.__den}'

    def __repr__(self):
        return f"Fraction('{self.__num}/{self.__den}')"

    def numerator(self, *args):
        if len(args):
            self.__num = args[0] * self.__sign()
            self.__reduction()
        return abs(self.__num)

    def __sign(self):
        return -1 if self.__num < 0 else 1

    def __gcd(self, a, b):
        while b:
            a, b = b, a % b
        return abs(a)

    def __reduction(self):
        gcd = self.__gcd(self.__num, self.__den)
        self.__num //= gcd
        self.__den //= gcd

        if self.__den < 0:
            self.__num = -self.__num
            self.__den = abs(self.__den)
        return self.__num, self.__den

    def denominator(self, *args):
        if len(args):
            self.__den = args[0]
        self.__reduction()
        return abs(self.__den)

    def reverse(self):
        return Fraction(self.__den, self.__num)
