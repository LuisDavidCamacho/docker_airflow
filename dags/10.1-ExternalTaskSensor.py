from airflow import DAG
from datetime import datetime
from airflow.operators.bash import BashOperator

with DAG(dag_id = "10.1_external_task_sensor",
         description = "using ExternalTaskSensor",
         start_date = datetime(2023, 3, 1),
         end_date = datetime(2023, 3, 14),
         schedule_interval = "@daily"
) as dag:

    task1 = BashOperator(task_id = "task1",
                         bash_command = "sleep 10 && echo 'DAG 1 finished'",
                         depends_on_past = True)

    task1

