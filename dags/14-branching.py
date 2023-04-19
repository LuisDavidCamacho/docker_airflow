from datetime import datetime, date
from airflow import DAG
from airflow.operators.python import BranchPythonOperator
from airflow.operators.bash import BashOperator

default_args = {'start_date': datetime(2023, 2, 1),
                'end_date': datetime(2023, 3, 1),}

def _choose(**context):
    if context["logical_date"].date() < date(2023, 2, 15):
        return "finish_14_feb" # Return the task_id to be executed
    return "start_15_feb"

with DAG(dag_id = "14_branching",
         description = "using BranchPythonOperator",
         schedule_interval = "@daily",
         default_args = default_args
) as dag:

    branching = BranchPythonOperator(task_id = "branch",
	                             python_callable = _choose)

    finish_14 = BashOperator(task_id = "finish_14_feb",
	                     bash_command = "echo 'Running {{ds}}'")

    start_15 = BashOperator(task_id = "start_15_feb",
	                    bash_command = "echo 'Running {{ds}}'")

    branching >> [finish_14, start_15]

