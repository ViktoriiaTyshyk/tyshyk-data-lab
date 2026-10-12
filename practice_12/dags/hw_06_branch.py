# Завдання 6 — Розгалуження
from datetime import datetime          
from airflow.sdk import dag, task


# Оголошуємо DAG, який вибирає одну з трьох гілок
@dag(
    dag_id="hw_06_branch",                # назва DAG в інтерфейсі
    start_date=datetime(2025, 1, 1),        # з якої дати рахуються запуски
    schedule=None,                          # запуск тільки вручну
    catchup=False,                          # не доганяти пропущені дати
    tags=["homework"],                      # мітка для фільтра у списку
)
def hw_06_branch():

    # отримання кількості рядків
    @task
    def count_rows():
        rows=4820
        print(f"Кількість рядків: {rows}")
        return rows

    # Вибираємо гілку залежно від кількості рядків
    @task.branch
    def choose_path(row_count):
        if row_count == 0:
            return "no_data"
        if row_count < 1000:
            return "load_small"
        return "load_big"

    # Гілка для малого обсягу даних
    @task
    def load_small():
        print("Loading small dataset")

    # Гілка для великого обсягу даних
    @task
    def load_big():
        print("Loading big dataset")

    # Гілка для випадку, коли даних немає
    @task
    def no_data():
        print("No data to load")

    # Створюємо задачі DAG
    row_count=count_rows()
    branch=choose_path(row_count)

    # Після choose_path виконається тільки вибрана гілка
    branch>>[no_data(), load_small(), load_big()]

hw_06_branch()