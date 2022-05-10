import streamlit as st
from log import save_field, read_field, save_logs
from solver import solve, deep_copy, check_field
import time


def create_sudoku():
    st.markdown('## Создание Судоку')
    st.write('Введите условие')

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
                field[j][i] = st.selectbox("", [_ for _ in range(10)], key=f"{i}{j}", format_func=lambda x: x if x != 0 else "")

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


def examples():
    st.markdown('## Примеры решенных cудоку')
    with open("examples.txt", encoding="utf-8") as f:
        text = f.read().split("-----------------------------------------")
        st.markdown("#### Первый пример - это простое судоку, которое не сложно решить самому.")
        st.text(text[0])
        st.write("#### Второй пример - это сложное судоку, которое трудно, но возможно решить самомоу. ")
        st.text(text[1])
        st.write("#### Третий пример - это судоку, состоящие только из 17 подсказок.\nДоказано, что задачи с меньшим количеством подсказок нельзя решить однозначно.")
        st.text(text[2])
        st.write("#### Четвертый пример - это пример судоку, которое невозможно решить.")
        st.text(text[3])
        st.write("#### Все примеры были взяты из логов. Если вы создадите такие-же задачи, программ выведет те-же ответы.")


