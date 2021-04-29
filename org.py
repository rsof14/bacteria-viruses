from abc import ABC, abstractmethod


class Org(ABC):  # абстрактный класс, от которого наследуют вирусы и бактерии
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols

    @abstractmethod
    def step(self):
        pass
