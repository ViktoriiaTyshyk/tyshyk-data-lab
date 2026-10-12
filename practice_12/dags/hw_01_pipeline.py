# Завдання 1 — перший пайплайн
from datetime import datetime          

from airflow.sdk import dag, task          


# Оголошуємо DAG - конвеєр, який об'єднує extract, transform та load задачі
@dag(
    dag_id="hw_01_pipeline",                # назва DAG в інтерфейсі
    start_date=datetime(2025, 1, 1),        # з якої дати рахуються запуски
    schedule=None,                          # запуск тільки вручну
    catchup=False,                          # не доганяти пропущені дати
    tags=["homework"],                      # мітка для фільтра у списку
)
def hw_01_pipeline():

    # Вхідні дані про виручку магазинів
    SALES = [
        {"store": "Київ", "amount": 1200.0},
        {"store": "Львів", "amount": 850.5},
        {"store": "Одеса", "amount": 430.25},
        {"store": "Київ", "amount": 610.0},
    ]

    # Завдання 1.1 - отримуємо початкові дані
    @task
    def extract(sales_data): 
        print(f"Кількість записів: {len(sales_data)}")                                    
        return sales_data

    # Завдання 1.2 - обчислюємо підсумкові показники
    @task
    def transform(sales_data):
        total = sum(sale["amount"] for sale in sales_data) 
        stores = len(set(sale["store"]for sale in sales_data))           
        rows=len(sales_data)
        return {"total": total, "stores": stores, "rows": rows}

    # Завдання 1.3 - виводимо результат обробки
    @task
    def load(result):
        print(f"Результат обробки: {result}")

    extracted_data = extract(SALES)                 # виклик задачі extract
    transformed_data = transform(extracted_data)  # виклик задачі transform
    load(transformed_data)  
                      
hw_01_pipeline()                            