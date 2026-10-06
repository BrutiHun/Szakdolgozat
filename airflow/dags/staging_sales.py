from datetime import datetime

from airflow import DAG
from airflow.providers.standard.operators.python import PythonOperator

from src.staging.sales import load_sales

with DAG(
    dag_id="staging_sales",
    start_date=datetime(2026,1,1),
    schedule=None
) as dag:
    load_sales_task= PythonOperator(
        task_id="load_sales",
        python_callable=load_sales

    )

