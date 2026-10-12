# Завдання 3 — Паралельні гілки
from datetime import datetime          
from airflow.sdk import dag, task 


# Оголошуємо DAG для паралельного виконання задач
@dag(
    dag_id="hw_03_parallel",                # назва DAG в інтерфейсі
    start_date=datetime(2025, 1, 1),        # з якої дати рахуються запуски
    schedule=None,                          # запуск тільки вручну
    catchup=False,                          # не доганяти пропущені дати
    tags=["homework"],                      # мітка для фільтра у списку
)
def hw_03_parallel():

    # Завдання 3.1 - повідомляємо про початок конвеєра
    @task
    def start():
        print("Start DAG")

    # Завдання 3.2 - завантажуємо дані про продажі
    @task
    def load_sales():
        return 1200

    # Завдання 3.2 - завантажуємо дані про магазини
    @task
    def load_stores():
        return 15

    # Завдання 3.2 - завантажуємо дані про товари
    @task
    def load_products():
        return 100

    # Завдання 3.3 - підсумовуємо результати
    @task
    def summarize(sales, stores, products):
        print(f"Sum: {sales + stores + products}")

    # Завдання 3.4 - створюємо задачі та задаємо залежності
    start_task = start()

    sales_task = load_sales()   
    stores_task = load_stores()
    products_task = load_products()

    start_task >> [sales_task, stores_task, products_task]    # Запускаємо три завантаження паралельно після start

    summarize(sales_task, stores_task, products_task)  # Передаємо всі результати для підсумовування

hw_03_parallel()
