class Fraction():
    def __init__(self, *args):
        if isinstance(args[0], str):
            self.__num, self.__den = [int(c) for c in args[0].split('/')]
        else:
            self.__num = args[0]
            self.__den = args[1]
        self.__reduction()

    def __sign(self):
        return -1 if self.__num < 0 else 1

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
        common_denominator = self.denominator() * other.denominator()
        self.__num = self.__num * other.__den + other.__num * self.__den
        self.__den = common_denominator
        self.__reduction()
        return self

    def __isub__(self, other):
        common_denominator = self.denominator() * other.denominator()
        self.__num = self.__num * other.__den - other.__num * self.__den
        self.__den = common_denominator
        self.__reduction()
        return self

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

    def __str__(self):
        return f'{self.__num}/{self.__den}'

    def __repr__(self):
        return f"Fraction('{self.__num}/{self.__den}')"

    def numerator(self, *args):
        if len(args):
            self.__num = args[0] * self.__sign()
            self.__reduction()
        return abs(self.__num)

    def denominator(self, *args):
        if len(args):
            self.__den = args[0]
        self.__reduction()
        return abs(self.__den)
