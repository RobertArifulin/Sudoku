def check_move(field: list, x: int, y: int, a: int) -> bool:
    row, column, block = get_info(field, x, y)
    if row.count(a) > 0 or column.count(a) > 0 or block.count(a) > 0:
        return False

    return True

