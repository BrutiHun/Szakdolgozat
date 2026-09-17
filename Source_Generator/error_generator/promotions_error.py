from generator_config import SEED, ERROR_RATE
import numpy as np
import pandas as pd
from pathlib import Path

rng = np.random.default_rng(SEED)

data_path = Path(__file__).parent.parent / "data"

promotions = pd.read_csv(data_path / "promotions.csv")

error= rng.random(len(promotions)) < ERROR_RATE
promotions["discount_percent"]=promotions["discount_percent"].astype(float)
promotions.loc[error,"discount_percent"]=promotions.loc[error,"discount_percent"]*0.01

date_formats=[
    "%Y-%m-%d",
    "%d/%m/%Y",
    "%m-%d-%Y",
    "%B %d, %Y",
    "%d %B %Y"
]

error= rng.random(len(promotions)) < ERROR_RATE
for index in promotions.index[error]:
    format=rng.choice(date_formats)
    promotions.loc[index,"start_date"]=pd.to_datetime(promotions.loc[index,"start_date"]).strftime(format)
    promotions.loc[index,"end_date"]=pd.to_datetime(promotions.loc[index,"end_date"]).strftime(format)




error= rng.random(len(promotions)) < ERROR_RATE
promotions.loc[error,["start_date","end_date"]]=promotions.loc[error,["end_date","start_date"]].values



promotions.to_csv(data_path / "promotions.csv", index=False, encoding="utf-8-sig")

