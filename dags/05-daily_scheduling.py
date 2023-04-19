from airflow import DAG
from datetime import datetime
from airflow.operators.bash import BashOperator

with DAG(dag_id = "05_daily_scheduling",
         description = "testing scheduling",
         start_date = datetime(2023, 2, 24),
         end_date = datetime(2023, 3, 24),
         schedule_interval = "@daily",
         default_args = {"depends_on_past": True},
         max_active_runs = 1
) as dag:

    task1 = BashOperator(task_id = "scheduled_task1",
                         bash_command = "sleep 2 && echo 'This is the task 1'")

    task2 = BashOperator(task_id = "scheduled_task2",
                         bash_command = "sleep 2 && echo 'This is the task 2'")

    task3 = BashOperator(task_id = "scheduled_task3",
                         bash_command = "sleep 2 && echo 'This is the task 3'")

    task4 = BashOperator(task_id = "scheduled_task4",
                         bash_command = "sleep 2 && echo 'This is the task 4'")

    task1 >> task2 >> [task3,task4]

