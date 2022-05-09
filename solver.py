from time import time


def deep_copy(field: list[list]) -> list[list]:  # производит глубокое копирование поля
    # эта функция в данном случае гораздо быстрее, чем deepcopy из модуля copy
    return [field[i].copy() for i in range(9)]


def get_options(x, y, field):  # возвращает возможные значения в заданной клетке
    possible = {1, 2, 3, 4, 5, 6, 7, 8, 9}
    for i in field[y]:  # строка
        possible.discard(i)
    for i in field:   # столбец
        possible.discard(i[x])
    x -= x % 3
    y -= y % 3
    for x2 in (x, x + 1, x + 2):  # квадрат
        for y2 in (y, y + 1, y + 2):
            possible.discard(field[y2][x2])
    return possible


def solve_logically(field: list[list]) -> tuple[list, bool]:  # заполняет максимальное количество клеток, используя логику
    field = deep_copy(field)
    change = True
    while change:
        change = False
        for x in range(9):
            for y in range(9):
                if not field[y][x]:
                    option = get_options(x, y, field)
                    if len(option) == 1:
                        field[y][x] = option.pop()
                        change = True
                    elif len(option) == 0:
                        return field, False
    return field, True


def solve(field: list[list]) -> tuple[list, bool]:  # решает рекурсивно
    field, res = solve_logically(field)
    if not res:
        return field, False
    x = -1
    y = -1
    for i in range(9):
        for j in range(9):
            if not field[i][j]:
                x = j
                y = i
                break
        if x != -1:
            break

    if x != -1:
        option = get_options(x, y, field)
        if len(option) == 0:  # судоку не решается
            return field, False
    else:  # если не была найдена пустая клетка
        return field, True
    for option in option:   # перебор вариантов
        field[y][x] = option
        new_field, res = solve(field)
        if res:
            return new_field, True
    return field, False


'''
пример ввода:

020070000
400000000
008004903
000108000
000400280
000050091
071020050
000300007
090000300
'''
