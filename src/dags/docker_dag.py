from airflow.decorators                         import task, dag
from airflow.providers.docker.operators.docker  import DockerOperator

from datetime import datetime

@dag(start_date=datetime(2023, 1, 1), schedule_interval='@daily', catchup=False)
def simple_docker_dag():

    @task()
    def t1():
        pass

    amass_enum = DockerOperator(
        task_id         = 'amass_enum',
        image           = 'caffix/amass',
        container_name  = 'amass_container',
        api_version     = 'auto',
        auto_remove     = True,
        command         = 'enum -share -d example.com', #customize logic in custom operator
        output_dir_path = '/.config/amass',
        docker_url      = 'unix://var/run/docker.sock',
        network_mode    = 'bridge',
    )

    t1 >> amass_enum
    