from pathlib import Path

import pandas as pd
from airflow.providers.postgres.hooks.postgres import PostgresHook


POSTGRES_CONN_ID = "retail_dwh"


def check_source(source_path: str):
    path = Path(source_path)

    if not path.exists():
        raise FileNotFoundError(
            f"Source file not found: {source_path}"
        )

    if path.stat().st_size == 0:
        raise ValueError(
            f"Source file is empty: {source_path}"
        )


def load_csv_to_staging(
    source_path: str,
    table_name: str,
    target_fields: list[str],
):
    df = pd.read_csv(source_path, dtype=str)

    hook = PostgresHook(
        postgres_conn_id=POSTGRES_CONN_ID
    )

    hook.run(f"TRUNCATE TABLE {table_name};")

    hook.insert_rows(
        table=table_name,
        rows=df.itertuples(
            index=False,
            name=None,
        ),
        target_fields=target_fields,
    )


def validate_staging(table_name: str):
    hook = PostgresHook(
        postgres_conn_id=POSTGRES_CONN_ID
    )

    row_count = hook.get_first(
        f"SELECT COUNT(*) FROM {table_name};"
    )[0]

    if row_count == 0:
        raise ValueError(
            f"Staging table is empty: {table_name}"
        )