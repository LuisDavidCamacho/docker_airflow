from airflow import DAG
from datetime import datetime
from airflow.operators.bash import BashOperator
from airflow.operators.python import PythonOperator
from airflow.utils.trigger_rule import TriggerRule

def myFunction():
    raise Exception

with DAG(dag_id = "09_trigger_rules",
         description = "using trigger rules",
         start_date = datetime(2023, 3, 1),
         end_date = datetime(2023, 3, 10),
         schedule_interval = "@daily",
         default_args = {},
         max_active_runs = 1
) as dag:

    task1 = BashOperator(task_id = "task1",
                         bash_command = "sleep 5 && echo 'This is the task 1'",
                         trigger_rule = TriggerRule.ALL_SUCCESS,
                         retries = 2,
                         retry_delay = 5,
                         depends_on_past = False)

    task2 = BashOperator(task_id = "task2",
                         bash_command = "sleep 3 && echo 'This is the task 2'",
                         trigger_rule = TriggerRule.ALL_SUCCESS,
                         retries = 2,
                         retry_delay = 5,
                         depends_on_past = True)

    task3 = BashOperator(task_id = "task3",
                         bash_command = "sleep 2 && echo 'This is the task 3'",
                         trigger_rule = TriggerRule.ALWAYS,
                         retries = 2,
                         retry_delay = 5,
                         depends_on_past = True)

    task4 = PythonOperator(task_id = "task4",
                           python_callable = myFunction,
                           trigger_rule = TriggerRule.ALL_SUCCESS,
                           retries = 2,
                           retry_delay = 5,
                           depends_on_past = True)

    task5 = BashOperator(task_id = "task5",
                         bash_command = "sleep 2 && echo 'This is the task 5'",
                         retries = 2,
                         retry_delay = 5,
                         depends_on_past = True)

    task1 >> task2 >> task3 >> task4 >> task5

