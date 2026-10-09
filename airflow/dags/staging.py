from datetime import datetime

from airflow import DAG
from airflow.providers.standard.operators.python import PythonOperator

from src.staging.staging_loader import (
    check_source,
    load_csv_to_staging,
    validate_staging,
)


STAGING_CONFIGS = {
    "staging_sales": {
        "source": "/opt/airflow/data/sales.csv",
        "table": "staging.sales",
        "fields": [
            "sales_id",
            "sales_date",
            "store_id",
            "customer_id",
            "product_id",
            "promotion_id",
            "quantity",
            "unit_price",
            "total_price",
            "payment_type",
        ],
    },
    "staging_stores": {
        "source": "/opt/airflow/data/stores.csv",
        "table": "staging.stores",
        "fields": [
            "store_id",
            "store_name",
            "store_type",
            "region_id",
        ],
    },
    "staging_customers": {
        "source": "/opt/airflow/data/loyalty_customers.csv",
        "table": "staging.loyalty_customers",
        "fields": [
            "customer_id",
            "first_name",
            "last_name",
            "gender",
            "birth_date",
            "region_id",
        ],
    },
    "staging_products": {
        "source": "/opt/airflow/data/products.csv",
        "table": "staging.products",
        "fields": [
            "product_id",
            "product_code",
            "category",
            "unit_price",
            "is_active",
        ],
    },
    "staging_promotions": {
        "source": "/opt/airflow/data/promotions.csv",
        "table": "staging.promotions",
        "fields": [
            "promotion_id",
            "product_id",
            "discount_percent",
            "promotion_name",
            "start_date",
            "end_date",
        ],
    },
    "staging_regions": {
        "source": "/opt/airflow/data/regions.csv",
        "table": "staging.regions",
        "fields": [
            "region_id",
            "country",
            "city",
        ],
    },
}


for dag_id, config in STAGING_CONFIGS.items():

    with DAG(
        dag_id=dag_id,
        start_date=datetime(2026, 1, 1),
        schedule=None,
        catchup=False,
        tags=["staging"],
    ) as dag:

        check = PythonOperator(
            task_id="check_source",
            python_callable=check_source,
            op_kwargs={
                "source_path": config["source"],
            },
        )

        load = PythonOperator(
            task_id="load_to_staging",
            python_callable=load_csv_to_staging,
            op_kwargs={
                "source_path": config["source"],
                "table_name": config["table"],
                "target_fields": config["fields"],
            },
        )

        validate = PythonOperator(
            task_id="validate_staging",
            python_callable=validate_staging,
            op_kwargs={
                "table_name": config["table"],
            },
        )

        check >> load >> validate

    globals()[dag_id] = dag