from generator_config import SEED, NUM_STORES, NUM_REGIONS
import numpy as np
import pandas as pd
from pathlib import Path

rng=np.random.default_rng(SEED)

store_types = [
    "Szupermarket",
    "Hipermarket",
    "Diszkont",
    "Kisbolt"
]

stores=[]
for i in range (1,NUM_STORES+1):


    stores.append({
        "store_id": i,
        "store_name": f"Üzlet {str(i).zfill(3)}",
        "store_type": rng.choice(store_types),
        "region_id": rng.integers(1, NUM_REGIONS+1)
    })

output_path = Path(__file__).parent.parent / "Data" / "stores.csv"
stores_df = pd.DataFrame(stores)
stores_df.to_csv(output_path, index=False, encoding="utf-8-sig")