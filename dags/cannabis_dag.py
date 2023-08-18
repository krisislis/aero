from datetime import timedelta

import pendulum
from airflow import DAG
from airflow.providers.docker.operators.docker import DockerOperator

from airflow.operators.dummy_operator import DummyOperator

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'retries': 3,
    'retry_delay': timedelta(minutes=10),
}

dag = DAG(
    dag_id='mr_dag',
    default_args=default_args,
    schedule_interval='0 */12 * * *',
    catchup=False,
    start_date=pendulum.now(),
)

start = DummyOperator(
    task_id='start',
    dag=dag,
)
end = DummyOperator(
    task_id='end',
    dag=dag,
)
task = DockerOperator(
    task_id='mr_dag',
    image='mr_dag',
    api_version='auto',
    command='python3 etls/cannabis.py',
    docker_url='unix://var/run/docker.sock',
    network_mode='host',
    user='airflow',
    dag=dag,
)

start >> task >> end
