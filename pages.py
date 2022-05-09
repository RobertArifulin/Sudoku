import streamlit as st
from log import save_field, read_field, save_logs
from solver import solve, deep_copy, check_field
import time


def create_sudoku():
    st.markdown('## Создание Судоку')
    st.write('Введите условие (0 - пустая клетка)')

    field = read_field()

    if st.button('Сохранить'):
        empty_count = 0
        for row in field:
            empty_count += row.count(0)
        if empty_count > 64:
            st.warning("Заполните хотя-бы 17 клеток")
        elif empty_count == 0:
            st.warning("Оставьте хотя-бы 1 клетку пустой")
        else:
            res = check_field(field)
            if res:
                st.warning("Успех")
                save_field(field, True)
            else:
                st.warning(f"Некорректный ввод")
        st.write(f"Заполнено: {81 - empty_count}")

    columns = st.columns(9)
    for i in range(9):
        with columns[i]:
            for j in range(9):
                field[j][i] = st.selectbox("", [_ for _ in range(10)], key=f"{i}{j}")

    save_field(field)


def solve_sudoku():
    st.markdown('## Решение Судоку')
    st.write('Нажмите Решить')

    field = read_field(True)
    display_field = ""
    for row in field:
        display_field += " ".join(map(str, row)) + "\n"

    st.text(display_field)

    empty_count = 0
    correct = True
    for row in field:
        empty_count += row.count(0)
    if empty_count > 64:
        st.warning("Некореткное условие")
        correct = False
    else:
        st.warning("Условие корректно")

    if st.button('Решить', disabled=not correct):
        start = time.time()
        field = deep_copy(read_field(True))
        solved_field, is_solved = solve(field)
        stop = round(time.time() - start, 4)
        save_logs(field, solved_field, is_solved, stop)

        if is_solved:
            st.write("Судоку было успешно решено: \n")
            display_field = ""
            for row in solved_field:
                display_field += " ".join(map(str, row)) + "\n"
            st.text(display_field)
            st.write(f"Решение заняло {stop} секунд \n")
        else:
            st.write("Судоку решить невозможно\n")

        with open("log.txt", "r", encoding="utf-8") as f:
            st.download_button("Скачать Логи", data=f, file_name="logs.txt", mime="txt")




