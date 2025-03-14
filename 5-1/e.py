class Rectangle:
    def __init__(self, a, b):
        self.first_side = abs(a[0] - b[0])
        self.second_side = abs(a[1] - b[1])

    def area(self):
        return round(self.first_side * self.second_side, 2)

    def perimeter(self):
        return round(2 * (self.first_side + self.second_side), 2)
