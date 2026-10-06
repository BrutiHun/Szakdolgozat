import pandas as pd

from airflow.providers.postgres.hooks.postgres import PostgresHook


SOURCE_PATH = "/opt/airflow/data/products.csv"


def load_products():
    df = pd.read_csv(SOURCE_PATH, dtype=str)

    hook = PostgresHook(postgres_conn_id="retail_dwh")
    hook.run("TRUNCATE TABLE staging.products;")

    hook.insert_rows(
        table="staging.products",
        rows=df.itertuples(index=False, name=None),
        target_fields=[
            "product_id",
            "product_code",
            "category",
            "unit_price",
            "is_active",
        ],
    )