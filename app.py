import streamlit as st
import os

class App:
    def __init__(self) -> None:
        self.pages = []

    def add_page(self, title, func) -> None:
        self.pages.append({
            "title": title,
            "function": func
        })

    def run(self):
        page = st.sidebar.selectbox(
            'Выбор страницы',
            self.pages,
            format_func=lambda page: page['title']
        )
        if not os.path.isfile("log.txt"):
            f = open("log.txt", "w", encoding="utf-8")
            f.close()
        with open("log.txt", "r", encoding="utf-8") as f:
            st.sidebar.download_button("Скачать Логи", data=f, file_name="logs.txt", mime="txt")

        page['function']()
