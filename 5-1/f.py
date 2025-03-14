class Rectangle:
    def __init__(self, a, b):
        self.top_corner = [max(a[0], b[0]), max(a[1], b[1])]
        self.bottom_corner = [min(a[0], b[0]), min(a[1], b[1])]

    def area(self):
        return round((self.top_corner[0] - self.bottom_corner[0]) *
                     (self.top_corner[1] - self.bottom_corner[1]), 2)

    def perimeter(self):
        return round((self.top_corner[0] - self.bottom_corner[0]) * 2 +
                     (self.top_corner[1] - self.bottom_corner[1]) * 2, 2)

    def get_pos(self):
        return round(self.bottom_corner[0], 2), round(self.top_corner[1], 2)

    def get_size(self):
        return (round((self.top_corner[0] - self.bottom_corner[0]), 2),
                round((self.top_corner[1] - self.bottom_corner[1]), 2))

    def move(self, move_x, move_y):
        self.top_corner[0] += move_x
        self.top_corner[1] += move_y
        self.bottom_corner[0] += move_x
        self.bottom_corner[1] += move_y

    def resize(self, width, height):
        self.top_corner[0] = self.bottom_corner[0] + width
        self.bottom_corner[1] = self.top_corner[1] - height
