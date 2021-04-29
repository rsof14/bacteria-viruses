from abc import ABC, abstractmethod
from random import randint
from org import Org
from bacteria import Bacteria


class Virus(Org):
    NAME = 'v'

    def __init__(self, field, rows, cols, i, j):
        super().__init__(rows, cols)
        self.field = field
        self.i = i
        self.j = j
        self.is_hungry = 0

    def die(self):  # функция, вызывающаяся, когда вирус умирает
        self.field[self.i][self.j] = None

    def eating(self):  # функция по поиску вирусом соседней бактерии и поеданию вирусом этой бактерии
        if self.i != 0 and isinstance(self.field[self.i - 1][self.j], Bacteria):
            self.field[self.i - 1][self.j] = None
            self.is_hungry = 0
            return self.share()
        if self.j != 0 and isinstance(self.field[self.i][self.j - 1], Bacteria):
            self.field[self.i][self.j - 1] = None
            self.is_hungry = 0
            return self.share()
        if self.i != self.rows - 1 and isinstance(self.field[self.i + 1][self.j], Bacteria):
            self.field[self.i + 1][self.j] = None
            self.is_hungry = 0
            return self.share()
        if self.j != self.cols - 1 and isinstance(self.field[self.i][self.j + 1], Bacteria):
            self.field[self.i][self.j + 1] = None
            self.is_hungry = 0
            return self.share()
        self.is_hungry += 1
        if self.is_hungry == 5:  # если вирус не ел 5 секунд, то он умирает
            self.die()
        return self.field

    def share(self):  # функция деления вируса с вероятностью 30%
        r = randint(0, 100)
        if r <= 30:
            x = randint(0, self.rows - 1)
            y = randint(0, self.cols - 1)
            while None in self.field and self.field[x][y] is not None:
                x = randint(0, self.rows - 1)
                y = randint(0, self.cols - 1)
            if self.field[x][y] is None:
                self.field[x][y] = Virus(self.field, self.rows, self.cols, x, y)
        return self.field

    def step(self):
        self.field = self.eating()
        return self.field
