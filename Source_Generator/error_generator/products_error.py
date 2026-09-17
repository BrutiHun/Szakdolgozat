from generator_config import SEED, ERROR_RATE
import numpy as np
import pandas as pd
from pathlib import Path

rng = np.random.default_rng(SEED)

data_path = Path(__file__).parent.parent / "data"

products = pd.read_csv(data_path / "products.csv")

error= rng.random(len(products)) < ERROR_RATE
products.loc[error,"category"]=np.nan

error= rng.random(len(products)) < ERROR_RATE
products.loc[error,"unit_price"]=np.nan

error= rng.random(len(products)) < ERROR_RATE
products.loc[error,"unit_price"]= products.loc[error,"unit_price"] * -1

error= rng.random(len(products)) < ERROR_RATE
products.loc[error,"category"]=rng.choice(["InvalidCategory1",
                                           "InvalidCategory2",
                                           "InvalidCategory3",
                                           "elektronika",
                                           "ruházat",
                                           "elelmiszer",
                                           "ital",
                                           "higiénia",
                                           "háztartás",
                                           "papír-írószer"],size=error.sum())

products["is_active"]=products["is_active"].astype(str)
error= rng.random(len(products)) < ERROR_RATE
products.loc[error,"is_active"]=rng.choice(["yes","no","0","1","igen","nem", ""],size=error.sum())

error= rng.random(len(products)) < ERROR_RATE
products=pd.concat([products,products.loc[error]],ignore_index=True)


products.to_csv(data_path / "products.csv", index=False, encoding="utf-8-sig")

