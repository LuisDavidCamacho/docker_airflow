from airflow import DAG
from datetime import datetime
from airflow.operators.empty import EmptyOperator

with DAG(dag_id = "07_monthly_scheduling",
         description = "testing scheduling",
         start_date = datetime(2023, 1, 1),
         end_date = datetime(2023, 3, 24),
         schedule_interval = "@monthly"
) as dag:

    task1 = EmptyOperator(task_id = "scheduled_task1")

    task2 = EmptyOperator(task_id = "scheduled_task2")

    task3 = EmptyOperator(task_id = "scheduled_task3")

    task4 = EmptyOperator(task_id = "scheduled_task4")

    task1 >> task2 >> task3 >> task4

