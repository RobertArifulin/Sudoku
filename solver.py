import time
from log import save_logs


def check_field(field: list[list]) -> bool:
    columns = [[0] * 9 for _ in range(9)]  # список столбцов
    for i in range(9):
        for j in range(9):
            columns[i][j] = field[j][i]
    blocks = [[] for _ in range(9)]  # список блоков
    for i in range(9):
        for j in range(9):
            blocks[3 * (i // 3) + j // 3].append(field[i][j])

    for i in range(9):  # Проверка на правильное кол-во цифр в:
        if len(set(columns[i])) - min(1, columns[i].count(0)) != 9 - columns[i].count(0):  # в колоннах
            return False
        if len(set(field[i])) - min(1, field[i].count(0)) != 9 - field[i].count(0):  # в рядах
            return False
        if len(set(blocks[i])) - min(1, blocks[i].count(0)) != 9 - blocks[i].count(0):  # в блоках
            return False

    for i in range(9):
        for j in range(9):
            if not field[i][j]:
                option = get_options(j, i, field)
                if not option:   # Проверка на правильность заполнения
                    return False
    return True


def deep_copy(field: list[list]) -> list[list]:  # производит глубокое копирование поля
    # эта функция в данном случае гораздо быстрее, чем deepcopy из модуля copy
    return [field[i].copy() for i in range(9)]


def get_options(x: int, y: int, field: list[list]) -> set:  # возвращает возможные значения в заданной клетке
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
    while change:  # пока что-то меняется
        change = False
        for x in range(9):
            for y in range(9):
                if not field[y][x]:
                    option = get_options(x, y, field)  # получаем возможные варианты
                    if len(option) == 1:  # если вариант 1 мы подставляем его
                        field[y][x] = option.pop()
                        change = True
                    elif len(option) == 0:
                        return field, False
    return field, True


def solve(field):  # решает рекурсивно
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
        new_field, res = solve(field)   # рекурсивный перебор
        if res:
            return new_field, True
    return field, False


def main():
    field1 = [[3, 2, 0, 4, 5, 0, 0, 0, 0], [5, 8, 9, 7, 6, 0, 2, 4, 0], [6, 1, 0, 8, 2, 9, 5, 3, 0],
              [4, 0, 1, 9, 3, 8, 0, 2, 0], [8, 7, 5, 6, 0, 0, 3, 9, 4], [9, 0, 0, 5, 4, 7, 6, 0, 8],
              [0, 9, 6, 0, 8, 5, 4, 7, 2], [0, 5, 8, 2, 0, 4, 1, 0, 3], [0, 4, 3, 0, 7, 6, 0, 5, 9]]

    field2 = [[3, 0, 7, 4, 0, 1, 0, 0, 0], [5, 8, 0, 0, 6, 0, 2, 0, 0], [0, 0, 0, 0, 2, 0, 5, 3, 7],
              [0, 0, 0, 0, 3, 0, 0, 2, 5], [0, 7, 0, 0, 0, 0, 0, 0, 4], [9, 0, 0, 5, 0, 7, 0, 1, 0],
              [0, 0, 0, 3, 0, 5, 0, 7, 0], [0, 0, 8, 0, 9, 4, 0, 0, 3], [2, 4, 0, 0, 0, 0, 8, 0, 0]]

    field3 = [[0, 0, 0, 8, 0, 1, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 4, 3], [5, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 7, 0, 8, 0, 0], [0, 0, 0, 0, 0, 0, 1, 0, 0], [0, 2, 0, 0, 3, 0, 0, 0, 0],
              [6, 0, 0, 0, 0, 0, 0, 7, 5], [0, 0, 3, 4, 0, 0, 0, 0, 0], [0, 0, 0, 2, 0, 0, 6, 0, 0]]

    field4 = [[8, 7, 6, 5, 4, 3, 2, 1, 0], [1, 2, 3, 4, 5, 6, 7, 8, 9], [0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0]]

    fields = [field1, field2, field3, field4]

    for field in fields:
        start = time.time()
        field = deep_copy(field)
        solved_field, is_solved = solve(field)
        stop = round(time.time() - start, 4)
        save_logs(field, solved_field, is_solved, stop)
        print(stop)


if __name__ == "__main__":
    main()
