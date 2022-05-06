def check_move(field: list, x: int, y: int, a: int) -> bool:
    row, column, block = get_info(field, x, y)
    if row.count(a) > 0 or column.count(a) > 0 or block.count(a) > 0:
        return False

    return True


def get_info(field: list[list], x: int, y: int) -> tuple[list, list, list]:
    row = field[y].copy()
    column = [field[i][x] for i in range(9)]
    block = []
    for i in range(9):
        for j in range(9):
            if x // 3 * 3 <= j < (x // 3 + 1) * 3 and y // 3 * 3 <= i < (
                    y // 3 + 1) * 3:  # Проверка на границы квадрата
                block.append(field[i][j])
    return row, column, block


def check_field(field: list):
    rows = []
    columns = [[] for i in range(9)]
    blocks = [[] for i in range(9)]
    for i in range(9):
        rows.append(field[i].copy())
        for j in range(9):
            columns[j].append(field[i][j])
            blocks[(j // 3) + 3 * (i // 3)].append(field[i][j])

    return rows, columns, blocks
