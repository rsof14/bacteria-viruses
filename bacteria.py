from abc import ABC, abstractmethod
from random import randint
from org import Org


class Bacteria(Org):
    NAME = 'b'

    def __init__(self, field, rows, cols, i, j):
        super().__init__(rows, cols)
        self.field = field
        self.i = i
        self.j = j

    def share(self): #функция деления с вероятностью 30%
        r = randint(0, 100)
        if r <= 30: #условие деления бактерии
            x = randint(0, self.rows - 1)
            y = randint(0, self.cols - 1)
            while None in self.field and self.field[x][y] is not None: #поиск места для новой бактерии
                x = randint(0, self.rows - 1)
                y = randint(0, self.cols - 1)
            if self.field[x][y] is None:
                self.field[x][y] = Bacteria(self.field, self.rows, self.cols, x, y) #создание экземпляра класса Бактерия в свободной клетке поля
        return self.field

    def step(self):
        self.field = self.share()
        return self.field
