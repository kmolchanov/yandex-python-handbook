class Programmer():
    def __init__(self, name, position):
        self.name = name
        self.position = position
        self.time_worked = 0
        self.payout = 0
        self.bonus = 0

    def work(self, time):
        rates = {
            'Junior': 10,
            'Middle': 15,
            'Senior': 20,
        }

        self.time_worked += time
        self.payout += (rates[self.position] + self.bonus) * time

    def rise(self):
        if self.position == 'Junior':
            self.position = 'Middle'
        elif self.position == 'Middle':
            self.position = 'Senior'
        elif self.position == 'Senior':
            self.bonus += 1

    def info(self):
        return f'{self.name} {self.time_worked}ч. {self.payout}тгр.'
