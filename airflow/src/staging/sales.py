import pandas as pd

from airflow.providers.postgres.hooks.postgres import PostgresHook

SOURCE_PATH = "/opt/airflow/data/sales.csv"

def load_sales():
    df=pd.read_csv(SOURCE_PATH,dtype=str)

    hook= PostgresHook(postgres_conn_id="retail_dwh")
    hook.run("TRUNCATE table staging.sales;")

    hook.insert_rows(
        table="staging.sales",
        rows=df.itertuples(index=False, name=None),
        target_fields=[
            "sales_id",
            "sales_date",
            "store_id",
            "customer_id",
            "product_id",
            "promotion_id",
            "quantity",
            "unit_price",
            "total_price",
            "payment_type"
        ]
    )