from airflow import DAG
from datetime import datetime
from airflow.operators.python import PythonOperator
from airflow.operators.bash import BashOperator

def print_hello():
  print('This is the task1')

with DAG(dag_id = "03_dependencies",
         description = "using tasks with dependencies",
         start_date = datetime(2023, 3, 24),
         schedule_interval = "@once"
) as dag:

    task1 = PythonOperator(task_id = "python_task1",
                           python_callable = print_hello)

    task2 = BashOperator(task_id = "bash_task2",
                         bash_command = "echo 'This is the task 2'")

    task3 = BashOperator(task_id = "bash_task3",
                         bash_command = "echo 'This is the task 3'")

    task4 = BashOperator(task_id = "bash_task4",
                         bash_command = "echo 'This is the task 4'")

    task1 >> task2 >> [task3,task4]
    
    # Another way to do it
    #task1.set_downstream(task2) 
    #task2.set_downstream([task3,task4])

