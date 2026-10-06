from datetime import datetime

from airflow import DAG
from airflow.providers.standard.operators.python import PythonOperator

from src.staging.customers import load_customers

with DAG(
    dag_id="staging_customers",
    start_date=datetime(2026,1,1),
    schedule=None
) as dag:
    load_customers_task= PythonOperator(
        task_id="load_customers",
        python_callable=load_customers

    )

