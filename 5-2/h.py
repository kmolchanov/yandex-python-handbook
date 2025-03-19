class Fraction():
    def __init__(self, *args):
        if isinstance(args[0], str):
            self.__num, self.__den = [int(c) for c in args[0].split('/')]
        else:
            self.__num = args[0]
            self.__den = args[1]
        self.__reduction()

    def __neg__(self):
        return Fraction(-self.__num, self.__den)

    def __add__(self, other):
        denominator = self.denominator() * other.denominator()
        numerator = self.__num * other.__den + other.__num * self.__den
        return Fraction(numerator, denominator)

    def __sub__(self, other):
        denominator = self.denominator() * other.denominator()
        numerator = self.__num * other.__den - other.__num * self.__den
        return Fraction(numerator, denominator)

    def __iadd__(self, other):
        self.__num = self.__num * other.__den + other.__num * self.__den
        self.__den = self.__den * other.__den
        self.__reduction()
        return self

    def __isub__(self, other):
        self.__num = self.__num * other.__den - other.__num * self.__den
        self.__den = self.__den * other.__den
        self.__reduction()
        return self

    def __mul__(self, other):
        denominator = self.__den * other.__den
        numerator = self.__num * other.__num
        return Fraction(numerator, denominator)

    def __truediv__(self, other):
        new = Fraction(self.__num, self.__den)
        return new.__mul__(other.reverse())

    def __imul__(self, other):
        self.__num = self.__num * other.__num
        self.__den = self.__den * other.__den
        self.__reduction()
        return self

    def __itruediv__(self, other):
        return self.__imul__(other.reverse())

    def __gt__(self, other):
        return self.__num * other.__den > other.__num * self.__den

    def __lt__(self, other):
        return self.__num * other.__den < other.__num * self.__den

    def __ge__(self, other):
        return self.__num * other.__den >= other.__num * self.__den

    def __le__(self, other):
        return self.__num * other.__den <= other.__num * self.__den

    def __eq__(self, other):
        return self.__num * other.__den == other.__num * self.__den

    def __ne__(self, other):
        return self.__num * other.__den != other.__num * self.__den

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
        __gcd = self.__gcd(self.__num, self.__den)
        self.__num //= __gcd
        self.__den //= __gcd

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
