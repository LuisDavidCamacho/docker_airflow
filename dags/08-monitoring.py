from airflow import DAG
from datetime import datetime
from airflow.operators.bash import BashOperator
from airflow.operators.python import PythonOperator

def myFunction():
    raise Exception

with DAG(dag_id = "08_monitoring",
         description = "monitoring a failed DAG",
         start_date = datetime(2023, 1, 1),
         end_date = datetime(2023, 2, 1),
         schedule_interval = "@daily"
) as dag:

    task1 = BashOperator(task_id = "scheduled_task1",
                         bash_command = "sleep 2 && echo 'This is the task 1'")

    task2 = BashOperator(task_id = "scheduled_task2",
                         bash_command = "sleep 2 && echo 'This is the task 2'")

    task3 = BashOperator(task_id = "scheduled_task3",
                         bash_command = "sleep 2 && echo 'This is the task 3'")

    task4 = PythonOperator(task_id = "scheduled_task4",
                           python_callable = myFunction)

    task5 = BashOperator(task_id = "scheduled_task5",
                         bash_command = "sleep 2 && echo 'This is the task 5'")

    task1 >> task2 >> task3 >> task4 >> task5

