import pandas as pd

from airflow.providers.postgres.hooks.postgres import PostgresHook

SOURCE_PATH = "/opt/airflow/data/stores.csv"

def load_stores():
    df=pd.read_csv(SOURCE_PATH,dtype=str)

    hook= PostgresHook(postgres_conn_id="retail_dwh")
    hook.run("TRUNCATE table staging.stores;")

    hook.insert_rows(
        table="staging.stores",
        rows=df.itertuples(index=False, name=None),
        target_fields=[
            "store_id",
            "store_name",
            "store_type",
            "region_id"
        ]
    )