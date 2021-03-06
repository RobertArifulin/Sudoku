import streamlit as st
from app import App
from pages import create_sudoku, solve_sudoku, examples


def main():
    app = App()
    st.markdown("# Судоку")

    app.add_page("Решение Судоку", solve_sudoku)
    app.add_page("Создание Судоку", create_sudoku)
    app.add_page("Примеры", examples)

    app.run()


main()
