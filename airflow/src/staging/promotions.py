import pandas as pd

from airflow.providers.postgres.hooks.postgres import PostgresHook

SOURCE_PATH = "/opt/airflow/data/promotions.csv"

def load_promotions():
    df=pd.read_csv(SOURCE_PATH,dtype=str)

    hook= PostgresHook(postgres_conn_id="retail_dwh")
    hook.run("TRUNCATE table staging.promotions;")

    hook.insert_rows(
        table="staging.promotions",
        rows=df.itertuples(index=False, name=None),
        target_fields=[
            "promotion_id",
            "product_id",
            "discount_percent",
            "promotion_name",
            "start_date",
            "end_date"
        ]
    )