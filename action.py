from random import randint
from org import Org
from bacteria import Bacteria
from virus import Virus
from output import Output


class Action():
    def __init__(self, field, rows, cols):
        self.field = field
        self.rows = rows
        self.cols = cols

    def is_end(self):  # функция, возвращающая True, если не все поле заполнено бактериями, и False в обратном случае
        for i in range(self.rows):
            for j in range(self.cols):
                if not isinstance(self.field[i][j], Bacteria):
                    return True
        return False

    def act(self):
        t = 0  # счетчик времени
        finish1 = []  # создаем пустую матрицу тех же размеров, что и поле
        for i in range(self.rows):
            row = []
            for j in range(self.cols):
                row.append(None)
            finish1.append(row)
        while self.field != finish1 and self.is_end():  # условие окончания симуляции: симуляци закончится, если поле пустое, либо поле заполнено бактериями
            t += 1
            for i in range(self.rows):
                for j in range(self.cols):
                    if self.field[i][j] is not None:
                        self.field = self.field[i][j].step()
            out = Output(self.field, self.rows, self.cols)
            out.matrix_output()
            print()
            print(f"После {t}-ой секунды ")
