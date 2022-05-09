import os


def save_logs(field, solved_field, is_solved, time):
    time = round(time, 4)
    idx = 1
    if os.path.isfile("log.txt"):
        f = open("log.txt", encoding="utf-8")
        s = f.read()
        idx = s.count("Условие") + 1
        f.close()
        f = open("log.txt", "a", encoding="utf-8")
    else:
        f = open("log.txt", "w", encoding="utf-8")

    f.write(f"Условие {idx}: \n")
    for row in field:
        f.write(" ".join(map(str, row)) + "\n")
    f.write("\n")
    if is_solved:
        f.write("Судоку было успешно решено: \n")
        for row in solved_field:
            f.write(" ".join(map(str, row)) + "\n")
        f.write(f"Решение заняло {time} секунд \n")
    else:
        f.write("Судоку решить невозможно\n")
    f.write("\n")
    f.write("-----------------------------------------\n")
    f.close()


def save_field(field, final=False):
    if final:
        f = open("save.txt", "w")
    else:
        f = open("source.txt", "w")
    for row in field:
        f.write("".join(map(str, row)) + "\n")
    f.close()


def read_field(final=False):
    if (os.path.isfile("save.txt") and final) or (os.path.isfile("source.txt") and not final):
        if final:
            f = open("save.txt")
        else:
            f = open("source.txt")
        s = f.read().split("\n")[:-1]

        if len(s) != 9:
            f.close()
            field = [[0] * 9 for _ in range(9)]
            save_field(field, final)
            return field

        field = []
        for row in s:
            field.append([])
            for i in row:
                field[-1].append(int(i))
        f.close()
    else:
        field = [[0] * 9 for _ in range(9)]
        save_field(field, final)

    return field
