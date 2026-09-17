from generator_config import SEED, ERROR_RATE
import numpy as np
import pandas as pd
from pathlib import Path

rng = np.random.default_rng(SEED)

data_path = Path(__file__).parent.parent / "data"

sales = pd.read_csv(data_path / "sales.csv")



error= rng.random(len(sales)) < min(ERROR_RATE*5,0.5)
sales.loc[error,"customer_id"]=np.nan

error= rng.random(len(sales)) < min(ERROR_RATE*5,0.5)
sales.loc[error,"promotion_id"]=np.nan


error= rng.random(len(sales)) < ERROR_RATE
sales.loc[error,"store_id"]=np.nan
error= rng.random(len(sales)) < ERROR_RATE
sales.loc[error,"store_id"]=rng.integers(9999, 99999, size=error.sum())

error= rng.random(len(sales)) < ERROR_RATE
sales.loc[error,"customer_id"]=np.nan
error= rng.random(len(sales)) < ERROR_RATE
sales.loc[error,"customer_id"]=rng.integers(9999, 99999, size=error.sum())

error= rng.random(len(sales)) < ERROR_RATE
sales.loc[error,"product_id"]=np.nan
error= rng.random(len(sales)) < ERROR_RATE
sales.loc[error,"product_id"]=rng.integers(9999, 99999, size=error.sum())

error= rng.random(len(sales)) < ERROR_RATE
sales.loc[error,"promotion_id"]=np.nan
error= rng.random(len(sales)) < ERROR_RATE
sales.loc[error,"promotion_id"]=rng.integers(9999, 99999, size=error.sum())

error= rng.random(len(sales)) < ERROR_RATE
sales.loc[error,"total_price"]=sales.loc[error,"total_price"]*rng.uniform(0.5,2,size=error.sum()).astype(int)

error= rng.random(len(sales)) < ERROR_RATE
sales.loc[error,"unit_price"]=sales.loc[error,"unit_price"]*rng.uniform(0.5,2,size=error.sum()).astype(int)

error= rng.random(len(sales)) < ERROR_RATE
sales.loc[error,"quantity"]=sales.loc[error,"quantity"]*-1
error= rng.random(len(sales)) < ERROR_RATE
sales.loc[error,"quantity"]=sales.loc[error,"quantity"]*0

error= rng.random(len(sales)) < ERROR_RATE
sales.loc[error,"quantity"]=np.nan

error= rng.random(len(sales)) < ERROR_RATE
sales.loc[error,"unit_price"]=np.nan

error= rng.random(len(sales)) < ERROR_RATE
sales.loc[error,"total_price"]=np.nan

payment_types=[
    "Error1",
    "Error2",
    "Error3",
    "készpénz",
    "bankkártya",
    "utalvány"
]
error= rng.random(len(sales)) < ERROR_RATE
sales.loc[error,"payment_type"]=rng.choice(payment_types,size=error.sum())


error= rng.random(len(sales)) < ERROR_RATE
sales.loc[error,"sales_date"]=(pd.to_datetime(sales.loc[error,"sales_date"])+pd.DateOffset(years=100)).dt.strftime("%Y-%m-%d")

error= rng.random(len(sales)) < ERROR_RATE
sales.loc[error,"sales_date"]=(pd.to_datetime(sales.loc[error,"sales_date"])+pd.DateOffset(years=-100)).dt.strftime("%Y-%m-%d")

date_formats=[
    "%Y-%m-%d",
    "%d/%m/%Y",
    "%m-%d-%Y",
    "%B %d, %Y",
    "%d %B %Y"
]

error= rng.random(len(sales)) < ERROR_RATE
for index in sales.index[error]:
    format=rng.choice(date_formats)
    sales.loc[index,"sales_date"]=pd.to_datetime(sales.loc[index,"sales_date"]).strftime(format)






error= rng.random(len(sales)) < ERROR_RATE
sales=pd.concat([sales,sales.loc[error]],ignore_index=True)



sales.to_csv(data_path / "sales.csv", index=False, encoding="utf-8-sig")

