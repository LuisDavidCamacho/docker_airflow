from airflow import DAG
from datetime import datetime
from airflow.operators.bash import BashOperator
from airflow.models.xcom import XCom
from airflow.operators.python import PythonOperator

def myFunction(**context):
    print(int(context["ti"].xcom_pull(task_ids='task2')) - 24)

with DAG(dag_id = "13_XCom",
         description = "using XCom",
         start_date = datetime(2023, 3, 1),
         end_date = datetime(2023, 3, 5),
         schedule_interval = "@daily",
         max_active_runs = 1,
         default_args = {"depends_on_past": True}
) as dag:

    task1 = BashOperator(task_id = "task1",
                         bash_command = "sleep 5 && echo $((3 * 8))")

    task2 = BashOperator(task_id = "task2",
                         bash_command = "sleep 3 && echo {{ ti.xcom_pull(task_ids='task1') }}")

    task3 = PythonOperator(task_id = "task3",
                           python_callable = myFunction)

    task1 >> task2 >> task3

