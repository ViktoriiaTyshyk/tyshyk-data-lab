# Завдання 4 — XCom
from datetime import datetime          
from airflow.sdk import dag, task, get_current_context 


# Оголошуємо DAG для демонстрації передачі значень через XCom
@dag(
    dag_id="hw_04_xcom",                # назва DAG в інтерфейсі
    start_date=datetime(2025, 1, 1),        # з якої дати рахуються запуски
    schedule=None,                          # запуск тільки вручну
    catchup=False,                          # не доганяти пропущені дати
    tags=["homework"],                      # мітка для фільтра у списку
)
def hw_04_xcom():

    # Завдання 4.1 - записуємо два значення в XCom
    @task
    def prepare_file():
        context=get_current_context()
        ti=context["ti"]
        ti.xcom_push(key="file_name", value="sales_2025_03.csv")
        ti.xcom_push(key="row_count", value=4820)
        print("Дані про файл збережено в XCom")

    # Завдання 4.2 - читаємо два значення з XCom
    @task
    def check_file():
        context=get_current_context()
        ti=context["ti"]
        file_name=ti.xcom_pull(task_ids="prepare_file", key="file_name")
        row_count=ti.xcom_pull(task_ids="prepare_file", key="row_count")
        print(f"File name: {file_name}, Row count: {row_count}")

    # задаємо послідовність виконання
    prepare_file()>>check_file()

hw_04_xcom()
