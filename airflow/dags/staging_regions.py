from datetime import datetime

from airflow import DAG
from airflow.providers.standard.operators.python import PythonOperator

from src.staging.regions import load_regions

with DAG(
    dag_id="staging_regions",
    start_date=datetime(2026,1,1),
    schedule=None
) as dag:
    load_regions_task= PythonOperator(
        task_id="load_regions",
        python_callable=load_regions

    )

