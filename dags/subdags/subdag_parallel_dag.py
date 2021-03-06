from airflow import DAG
from airflow.operators.bash import BashOperator


def subdag_parallel_dag(parent_dag_id,child_dag_id, default_args ):
    with DAG(dag_id=f'{parent_dag_id}.{child_dag_id}', default_args= default_args) as dag:

        task_5 = BashOperator(
            task_id = 'task_5',
            bash_command = 'sleep 3'
        )

        task_6 = BashOperator(
            task_id = 'task_6',
            bash_command = 'sleep 3'
        )

        return dag
