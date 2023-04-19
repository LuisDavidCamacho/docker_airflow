from airflow import DAG
from datetime import datetime
from airflow.operators.bash import BashOperator
from airflow.sensors.external_task import ExternalTaskSensor

with DAG(dag_id = "10.2_external_task_sensor",
         description = "using ExternalTaskSensor",
         start_date = datetime(2023, 3, 1),
         end_date = datetime(2023, 3, 14),
         schedule_interval = "@daily",
         max_active_runs = 1
) as dag:

    task1 = ExternalTaskSensor(task_id = "waiting_task",
                               external_dag_id = "10.1_external_task_sensor",
                               external_task_id = "task1",
                               poke_interval = 10) # Ask each 10 seconds if task1 has finished

    task2 = BashOperator(task_id = "task2",
                         bash_command = "sleep 10 && echo 'DAG 2 finished'",
                         depends_on_past = True)

    task1 >> task2

