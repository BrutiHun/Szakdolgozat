from generator_config import SEED,NUM_PROMOTIONS,NUM_PRODUCTS
import numpy as np
from pathlib import Path
import pandas as pd
from datetime import date, timedelta

rng=np.random.default_rng(SEED)

names=[
    "Kiemelt akció",
    "Hétvégi akció",
    "Ünnepi akció",
    "Nyári akció",
    "Téli akció",
    "Tavaszi akció",
    "Őszi akció"
]

promotions=[]
for i in range (1,NUM_PROMOTIONS+1):
    
    start_date =date(2026,1,1)+timedelta(days=int(rng.integers(0, 365)))
    end_date = start_date + timedelta(days=int(rng.integers(1, 30)))
    promotions.append({
        "promotion_id": i,
        "product_id":rng.integers(1, NUM_PRODUCTS+1),
        "discount_percent":rng.integers(5, 51),
        "promotion_name":rng.choice(names),
        "start_date": start_date,
        "end_date": end_date
        })


    

output_path = Path(__file__).parent.parent / "Data" / "promotions.csv"
promotions = pd.DataFrame(promotions)
promotions.to_csv(output_path, index=False, encoding="utf-8-sig")