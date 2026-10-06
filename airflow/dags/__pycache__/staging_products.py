from datetime import datetime

from airflow import DAG
from airflow.providers.standard.operators.python import PythonOperator

from src.staging.products import load_products


with DAG(
    dag_id="staging_products",
    start_date=datetime(2026, 1, 1),
    schedule=None,
    catchup=False,
) as dag:

    load_products_task = PythonOperator(
        task_id="load_products",
        python_callable=load_products,
    )