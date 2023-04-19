from airflow import DAG
from datetime import datetime
from airflow.operators.empty import EmptyOperator

with DAG(dag_id = "00_first_dag",
         description = "my first dag",
         start_date = datetime(2023, 3, 23),
         schedule_interval = "@once"
) as dag:

    task = EmptyOperator(task_id = "dummy_task")

    task

