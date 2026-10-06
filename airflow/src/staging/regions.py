import pandas as pd

from airflow.providers.postgres.hooks.postgres import PostgresHook

SOURCE_PATH = "/opt/airflow/data/regions.csv"

def load_regions():
    df=pd.read_csv(SOURCE_PATH,dtype=str)

    hook= PostgresHook(postgres_conn_id="retail_dwh")
    hook.run("TRUNCATE table staging.regions;")

    hook.insert_rows(
        table="staging.regions",
        rows=df.itertuples(index=False, name=None),
        target_fields=[
            "region_id",
            "country",
            "city"
        ]
    )