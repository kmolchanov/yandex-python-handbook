class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move(self, move_x, move_y):
        self.x += move_x
        self.y += move_y

    def length(self, point):
        result = round(((self.x - point.x) ** 2 + (self.y - point.y) ** 2) ** 0.5, 2)

        return result


class PatchedPoint(Point):
    def __init__(self, *args):
        match len(args):
            case 0:
                super().__init__(0, 0)
            case 1:
                super().__init__(*args[0])
            case 2:
                super().__init__(*args)
