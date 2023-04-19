from airflow import DAG
from datetime import datetime
from airflow.operators.bash import BashOperator
from airflow.sensors.filesystem import FileSensor

# IMPORTANT!
# You must create a File (Path) type connection called fs_default in Airflow ir order to run this DAG successfullys

with DAG(dag_id = "11_file_sensor",
         description = "using FileSensor",
         start_date = datetime(2023, 3, 20),
         end_date = datetime(2023, 3, 24),
         schedule_interval = "@daily",
         max_active_runs = 1
) as dag:

    task1 = BashOperator(task_id = "create_file_task",
                         bash_command = "sleep 10 && touch /tmp/file.txt")

    task2 = FileSensor(task_id = "waiting_file_task",
                       filepath = "/tmp/file.txt")

    task3 = BashOperator(task_id = "end_task",
                         bash_command = "echo 'The file has arrived'")

    task1 >> task2 >> task3

