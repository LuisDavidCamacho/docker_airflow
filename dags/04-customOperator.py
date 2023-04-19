from airflow import DAG
from datetime import datetime
from src.hellooperator import HelloOperator

with DAG(dag_id = "04_customOperator",
         description = "using custom (base) operator",
         start_date = datetime(2023, 3, 24),
         schedule_interval = "@once"
) as dag:

    task = HelloOperator(task_id = "hello_with_custom_operator",
                         name = "KLYMers")

    task

