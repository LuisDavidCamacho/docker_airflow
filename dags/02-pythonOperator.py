from airflow import DAG
from datetime import datetime
from airflow.operators.python import PythonOperator

def print_hello():
  print('Hello KLYMers from Python function')

with DAG(dag_id = "02_pythonOperator",
         description = "using python operator",
         start_date = datetime(2023, 3, 23),
         schedule_interval = "@once"
) as dag:

    task = PythonOperator(task_id = "hello_with_python",
                          python_callable = print_hello)

    task

