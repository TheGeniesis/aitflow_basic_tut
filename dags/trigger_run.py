from airflow.models import DAG
from airflow.providers.sqlite.operators.sqlite import SqliteOperator
from airflow.providers.http.sensors.http import HttpSensor
from airflow.providers.http.operators.http import SimpleHttpOperator
from airflow.operators.python import PythonOperator
from airflow.operators.bash import BashOperator

from datetime import datetime
from pandas import json_normalize
import json

default_args = {
  'start_date': datetime(2020,1,1)
}
 
 
with DAG('trigger_rule', schedule_interval='@daily', default_args=default_args, catchup=False)  as dag:
# tasks/operators
    task_1 =  BashOperator (
        task_id = 'task_1',
        do_xcom_push=False,
        bash_command= 'exit 0'
    )

    task_2 =  BashOperator (
        task_id = 'task_2',
        do_xcom_push=False,
        bash_command= 'exit 1'
    )

    task_3 =  BashOperator (
        task_id = 'task_3',
        do_xcom_push=False,
        bash_command= 'exit 0',
        # trigger_rule='all_done'
        trigger_rule='one_failed'
    )

    [task_1, task_2] >> task_3
