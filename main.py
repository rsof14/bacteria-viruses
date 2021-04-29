from abc import ABC, abstractmethod
from random import randint
from virus import Virus
from bacteria import Bacteria
from output import Output
from action import Action


class main:  # считываем данные, создаем поле
    cols, rows = map(int, input("Введите размеры поля ").split())  # размеры поля
    bact = int(input("Введите количество бактерий "))  # ввод количества бактерий
    virus = int(input("Введите количество вирусов "))  # ввод количества вирусов
    field = []  # создаем пустое поле
    for i in range(rows):
        row = []
        for j in range(cols):
            row.append(None)
        field.append(row)
    x = randint(0, rows - 1)
    y = randint(0, cols - 1)
    for i in range(bact):  # заполняем поле бактериями в случайном порядке
        while field[x][y] is not None:
            x = randint(0, rows - 1)
            y = randint(0, cols - 1)
        field[x][y] = Bacteria(field, rows, cols, x, y)  # создаем экземпляр класса Бактерия для каждой бактерии
    for i in range(virus):  # заполняем поле вирусами в случайном порядке
        while field[x][y] is not None:
            x = randint(0, rows - 1)
            y = randint(0, cols - 1)
        field[x][y] = Virus(field, rows, cols, x, y)  # создаем экземпляр класса Вирус для каждого вируса
    out = Output(field, rows, cols)
    out.matrix_output()  # выводим начальную матрицу
    print("Начальное поле")
    act = Action(field, rows, cols)
    act.act()  # запускаем симуляцию


if __name__ == "__main__":
    main()
