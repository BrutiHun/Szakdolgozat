from datetime import datetime

from airflow import DAG
from airflow.providers.standard.operators.python import PythonOperator

from src.staging.promotions import load_promotions

with DAG(
    dag_id="staging_promotions",
    start_date=datetime(2026,1,1),
    schedule=None
) as dag:
    load_promotions_task= PythonOperator(
        task_id="load_promotions",
        python_callable=load_promotions

    )

