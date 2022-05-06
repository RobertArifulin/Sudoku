from time import time


def deep_copy(grid): # производит глубокое копирование поля
    # эта функция в данном случае гораздо быстрее, чем deepcopy из модуля copy
    return [grid[i].copy() for i in range(9)]


def get_options(x, y, grid): # возвращает возможные значения в заданной клетке
    possible = {1, 2, 3, 4, 5, 6, 7, 8, 9}
    for i in grid[y]:
        possible.discard(i)
    for i in grid:
        possible.discard(i[x])
    x -= x % 3
    y -= y % 3
    for x2 in (x, x + 1, x + 2):
        for y2 in (y, y + 1, y + 2):
            possible.discard(grid[y2][x2])
    return possible


def solve_logically(grid): # заполняет максимальное количество клеток, используя логику
    grid = deep_copy(grid)
    flag = True
    while flag:
        flag = False
        for x in range(9):
            for y in range(9):
                if not grid[y][x]:
                    obtions = get_options(x, y, grid)
                    if len(obtions) == 1:
                        grid[y][x] = obtions.pop()
                        flag = True
    return grid


def solve(grid): # решает рекурсивно
    grid = solve_logically(grid)
    for i in range(9):
        if 0 in grid[i]:
            x = grid[i].index(0)
            break
    try:
        option = get_options(x, i, grid)
    except NameError:  # если не была найдена пустая клетка
        return grid
    for option in option:
        grid[i][x] = option
        result = solve(grid)
        if result:
            return result


#grid = [[int(j) for j in ' '.join(input()).split()] for i in range(9)]
grid = [[0, 0, 0, 8, 0, 1, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 4, 3], [5, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 7, 0, 8, 0, 0], [0, 0, 0, 0, 0, 0, 1, 0, 0], [0, 2, 0, 0, 3, 0, 0, 0, 0],
          [6, 0, 0, 0, 0, 0, 0, 7, 5], [0, 0, 3, 4, 0, 0, 0, 0, 0], [0, 0, 0, 2, 0, 0, 6, 0, 0]]
start = time()
print()
for i in solve(grid):
    print(i)
print()
print('time spent:', time() - start)




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
