# Завдання 2 — Класичні оператори
from datetime import datetime          
from airflow.providers.standard.operators.empty import EmptyOperator
from airflow.providers.standard.operators.bash import BashOperator
from airflow.providers.standard.operators.python import PythonOperator
from airflow.sdk import dag 

def report(store, amount):          #функція для make_report
    print(f"Store: {store}, Amount: {amount}")

#DAG в якому задачі створюються не декоратором, а готовими операторами
@dag(
    dag_id="hw_02_operators",                # назва DAG в інтерфейсі
    start_date=datetime(2025, 1, 1),        # з якої дати рахуються запуски
    schedule=None,                          # запуск тільки вручну
    catchup=False,                          # не доганяти пропущені дати
    tags=["homework"],                      # мітка для фільтра у списку
)
def hw_02_operators():

    start=EmptyOperator(task_id="start")  # початок DAG

    show_date=BashOperator(task_id="show_date", bash_command="date")  # виконуємо команду date

    count_dags=BashOperator(task_id="count_dags", bash_command="ls /opt/airflow/dags | wc -l")  # рахуємо кількість файлів у папці dags

    make_report=PythonOperator(task_id="make_report", python_callable=report, op_kwargs={"store": "Київ", "amount": 1810.0})  # викликаємо функцію report

    finish=EmptyOperator(task_id="finish")  # кінець DAG

    start>>[show_date, count_dags]>>make_report>>finish  # визначаємо порядок виконання задач

hw_02_operators()  

