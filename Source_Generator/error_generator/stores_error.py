from generator_config import SEED, ERROR_RATE
import numpy as np
import pandas as pd
from pathlib import Path

rng = np.random.default_rng(SEED)

data_path = Path(__file__).parent.parent / "data"

stores = pd.read_csv(data_path / "stores.csv")



error= rng.random(len(stores)) < ERROR_RATE
stores.loc[error,"region_id"]=np.nan

error= rng.random(len(stores)) < ERROR_RATE
stores.loc[error,"region_id"]=stores.loc[error,"region_id"]*-1

error= rng.random(len(stores)) < ERROR_RATE
stores.loc[error,"region_id"]=rng.integers(999, 9999, size=error.sum())

error= rng.random(len(stores)) < ERROR_RATE
stores.loc[error,"store_type"]=rng.choice(["InvalidType1",
                                           "InvalidType2",
                                           "InvalidType3",
                                           "szupermarket",
                                           "hipermarket",
                                           "diszkont",
    "Kisbolt"],size=error.sum())

stores.to_csv(data_path / "stores.csv", index=False, encoding="utf-8-sig")

