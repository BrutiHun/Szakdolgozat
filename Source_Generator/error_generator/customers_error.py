from generator_config import SEED, ERROR_RATE
import numpy as np
import pandas as pd
from pathlib import Path

rng = np.random.default_rng(SEED)

data_path = Path(__file__).parent.parent / "data"

customers = pd.read_csv(data_path / "loyalty_customers.csv")



error= rng.random(len(customers)) < ERROR_RATE
customers.loc[error,"region_id"]=np.nan

error= rng.random(len(customers)) < ERROR_RATE
customers.loc[error,"region_id"]=customers.loc[error,"region_id"]*-1

error= rng.random(len(customers)) < ERROR_RATE
customers.loc[error,"region_id"]=rng.integers(999, 9999, size=error.sum())

error= rng.random(len(customers)) < ERROR_RATE
customers.loc[error,"birth_date"]=(pd.to_datetime(customers.loc[error,"birth_date"])+pd.DateOffset(years=100)).dt.strftime("%Y-%m-%d")

error= rng.random(len(customers)) < ERROR_RATE
customers.loc[error,"birth_date"]=(pd.to_datetime(customers.loc[error,"birth_date"])+pd.DateOffset(years=-100)).dt.strftime("%Y-%m-%d")

error= rng.random(len(customers)) < ERROR_RATE


date_formats=[
    "%Y-%m-%d",
    "%d/%m/%Y",
    "%m-%d-%Y",
    "%B %d, %Y",
    "%d %B %Y"
]

error= rng.random(len(customers)) < ERROR_RATE
for index in customers.index[error]:
    format=rng.choice(date_formats)
    customers.loc[index,"birth_date"]=pd.to_datetime(customers.loc[index,"birth_date"]).strftime(format)    

error= rng.random(len(customers)) < ERROR_RATE
customers.loc[error,"gender"]=rng.choice(["Male","Female","","M","F"],size=error.sum())


customers.to_csv(data_path / "loyalty_customers.csv", index=False, encoding="utf-8-sig")

