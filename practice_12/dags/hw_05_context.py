# Завдання 5 — Контекст запуску і дата
from datetime import datetime         
from airflow.providers.standard.operators.bash import BashOperator 
from airflow.sdk import dag, task, get_current_context 


# Оголошуємо DAG для роботи з контекстом і датами
@dag(
    dag_id="hw_05_context",                # назва DAG в інтерфейсі
    start_date=datetime(2025, 1, 1),        # з якої дати рахуються запуски
    schedule=None,                          # запуск тільки вручну
    catchup=False,                          # не доганяти пропущені дати
    tags=["homework"],                      # мітка для фільтра у списку
)
def hw_05_context():

    # Завдання 5.1 - показуємо інформацію з контексту запуску
    @task
    def show_context():
        context=get_current_context()
        print("dag_id: ", context["dag"].dag_id)
        print("task_id: ", context["ti"].task_id)
        print("run_type: ", context["dag_run"].run_type)
        print("date: ", context["logical_date"])

    # Завдання 5.2 - виводимо логічну дату через шаблон Airflow
    echo_date = BashOperator(
        task_id="echo_date",  
        bash_command='echo "Логічна дата: {{ ds }}"',  
    )

    # Завдання 5.3 - формуємо шлях до файлу на основі логічної дати
    @task
    def build_path():
        context=get_current_context()
        logical_date=context["logical_date"]
        if logical_date is None:
            date_part = datetime.now().strftime("%Y-%m-%d")  # Використовуємо поточну дату, якщо логічної немає
        else:
            date_part = logical_date.strftime("%Y-%m-%d")  

        path = f"/data/sales/{date_part}.csv"  # Формуємо шлях до CSV-файлу
        print(f"Шлях до файлу: {path}")  

    show_context() >> echo_date >> build_path()  # визначаємо порядок виконання задач

hw_05_context()

