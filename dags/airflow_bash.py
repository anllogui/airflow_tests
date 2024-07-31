from airflow import DAG
from airflow.operators.bash import BashOperator

from datetime import datetime, timedelta

default_args = {
    'owner': 'anllogui',
    'retries' : 5,
    'retry_delay' : timedelta(minutes=2)
}
with DAG(
    dag_id = 'first_dag_v4',
    description= 'this is the first dag',
    default_args=default_args,
    start_date=datetime(2024, 7, 31, 2),
    schedule_interval='@daily'
    ) as dag:
    
    task1 = BashOperator(
        task_id = 'first_task',
        bash_command="echo hello world, this is the first task!"
    )
    
    task2 = BashOperator(
        task_id = 'second_task',
        bash_command="echo hello world, this is the second task!"
    )
    
    task3 = BashOperator(
        task_id = 'third_task',
        bash_command="echo hello world, this is the third task!"
    )

    # task dependencies
        
    # task1.set_downstream(task2)
    # task1.set_downstream(task3)
    
    # task1 >> task2
    # task1 >> task3
    
    task1 >> [task2, task3]
    