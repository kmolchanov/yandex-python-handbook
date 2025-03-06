class RedButton:
    def __init__(self):
        self.clicked = 0

    def click(self):
        print('Тревога!')
        self.clicked += 1

    def count(self):
        return self.clicked
