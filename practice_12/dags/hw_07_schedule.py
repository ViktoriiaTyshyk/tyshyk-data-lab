# Завдання 7 — Розклад
from datetime import datetime          
from airflow.sdk import dag, task, get_current_context


# Оголошуємо DAG, який автоматично запускається кожні 5 хвилин
@dag(
    dag_id="hw_07_schedule",                # назва DAG в інтерфейсі
    start_date=datetime(2025, 1, 1),        # з якої дати рахуються запуски
    schedule="*/5 * * * *",                     
    catchup=False,                          # не доганяти пропущені дати
    max_active_runs=1,                     # обмежуємо кількість одночасних запусків
    tags=["homework"],                      # мітка для фільтра у списку
)
def hw_07_schedule():

    # Виводимо інформацію про поточний запуск DAG
    @task
    def heartbeat():
        context=get_current_context()
        print(f"Date: {context["logical_date"]}, run_type: {context["dag_run"].run_type}")

    # Створюємо задачу
    heartbeat()

hw_07_schedule()

#Завдання 7.2
# Розклад Airflow: Every 5 minutes
# Наступний запуск DAG після 2026-10-13 01:45:00 буде о 2026-10-13 01:50:00

#Завдання 7.4

# 0 7 * * 1-5      cron
# Розклад Airflow: At 07:00, Monday through Friday
# Наступний запуск DAG 2026-10-13 10:00:00

# 0 */6 * * *      cron
# Розклад Airflow: Every 6 hours
# Наступний запуск DAG після 2026-10-12 21:00:00 буде о 2026-10-13 03:00:00

# @hourly          скорочення
# Розклад Airflow: Every hour
# Наступний запуск DAG після 2026-10-13 02:00:00 буде о 2026-10-13 03:00:00

#Завдання 7.5
# 3 запуски



