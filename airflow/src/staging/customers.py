import pandas as pd

from airflow.providers.postgres.hooks.postgres import PostgresHook

SOURCE_PATH = "/opt/airflow/data/loyalty_customers.csv"

def load_customers():
    df=pd.read_csv(SOURCE_PATH,dtype=str)

    hook= PostgresHook(postgres_conn_id="retail_dwh")
    hook.run("TRUNCATE table staging.loyalty_customers;")

    hook.insert_rows(
        table="staging.loyalty_customers",
        rows=df.itertuples(index=False, name=None),
        target_fields=[
            "customer_id",
            "first_name",
            "last_name",
            "gender",
            "birth_date",
            "region_id"
        ]
    )