from airflow import DAG
from datetime import datetime
from airflow.operators.bash import BashOperator

with DAG(dag_id = "01_bashOperator",
         description = "using batch operator",
         start_date = datetime(2023, 3, 23),
         schedule_interval = "@once"
) as dag:

    task = BashOperator(task_id = "hello_with_bash",
                        bash_command = "echo 'Hello KLYMers'")

    task

