from bacteria import Bacteria
from virus import Virus


class Output():
    def __init__(self, field, rows, cols):
        self.field = field
        self.cols = cols
        self.rows = rows

    def matrix_output(self):
        for i in range(self.rows):
            for j in range(self.cols):
                print("+-", end="")
            print("+")
            print("|", end="")
            for j in range(self.cols):
                if self.field[i][j] is None:
                    print(' ', end="|")
                else:
                    if isinstance(self.field[i][j], Bacteria):
                        print(Bacteria.NAME, end="|")
                    if isinstance(self.field[i][j], Virus):
                        print(Virus.NAME, end="|")
            print()
        for j in range(self.cols):
            print("+-", end="")
        print("+")
