from airflow import DAG
from datetime import datetime
from airflow.operators.bash import BashOperator


# {{ ds }} represents the DAG run's logical date
templated_command = """
{% for file in params.filenames %}
    echo "{{ ds }}"
    echo "{{ file }}"
{% endfor %}
"""

with DAG(dag_id = "12_templating",
         description = "using Jinja templates",
         start_date = datetime(2023, 3, 1),
         end_date = datetime(2023, 3, 5),
         schedule_interval = "@daily",
         max_active_runs = 1
) as dag:

    task1 = BashOperator(task_id = "task1",
                         bash_command = templated_command,
                         params = {"filenames": ["file1.txt", "file2.txt"]},
                         depends_on_past = True)

    task1

