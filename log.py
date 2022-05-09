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

