from airflow.models import DAG
from airflow.operators.subdag import SubDagOperator
from airflow.operators.bash import BashOperator
from airflow.utils.task_group import TaskGroup

from datetime import datetime
from pandas import json_normalize
import json

from subdags.subdag_parallel_dag import subdag_parallel_dag

default_args = {
  'start_date': datetime(2020,1,1)
}

with DAG('parallel_dag', schedule_interval='@daily', concurrency=1, max_active_runs=1, default_args=default_args, catchup=False)  as dag:
# tasks/operators

    task_1 = BashOperator(
        task_id = 'task_1',
        bash_command = 'sleep 3'
    )

    task_2 = BashOperator(
        task_id = 'task_2',
        bash_command = 'sleep 3'
    )

    task_3 = BashOperator(
        task_id = 'task_3',
        bash_command = 'sleep 3'
    )

    task_4 = BashOperator(
        task_id = 'task_4',
        bash_command = 'sleep 3'
    )

    processing = SubDagOperator(
        task_id = 'processing_sub_tasks',
        subdag = subdag_parallel_dag('parallel_dag', 'processing_sub_tasks', default_args)
    )

    with TaskGroup('processing_tasks') as processing_tasks:
        task_7 = BashOperator(
            task_id = 'task_7',
            bash_command = 'sleep 3'
        )

        task_8 = BashOperator(
            task_id = 'task_8',
            bash_command = 'sleep 3'
        )
    

    task_1 >> processing_tasks >> task_4
    #task_1 >> processing >> task_4
    # task_1 >> [task_2, task_3] >> task_4
