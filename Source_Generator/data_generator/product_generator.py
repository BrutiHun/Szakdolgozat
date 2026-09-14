from generator_config import SEED,NUM_PRODUCTS
import numpy as np
from pathlib import Path
import pandas as pd

rng=np.random.default_rng(SEED)
price_ranges = {
    "Élelmiszer": (100, 5000),
    "Ital": (150, 3000),
    "Háztartás": (500, 15000),
    "Higiénia": (300, 10000),
    "Elektronika": (5000, 100000),
    "Ruházat": (2000, 50000),
    "Papír-írószer": (100, 5000),
}

categories=[
    "Elektronika",
    "Ruházat",
    "Élelmiszer",
    "Ital",
    "Higiénia",
    "Háztartás",
    "Papír-írószer"
]
products=[]
for i in range (1,NUM_PRODUCTS+1):
    category=rng.choice(categories)
    min_price, max_price=price_ranges[category]



    products.append({
        "product_id": i,
        "product_code": f"P{str(i).zfill(4)}",
        "category": category,
        "unit_price": rng.integers(min_price, max_price+1),
        "is_active": rng.choice([True, False], p=[0.9, 0.1])
    })

output_path = Path(__file__).parent.parent / "Data" / "products.csv"
products = pd.DataFrame(products)
products.to_csv(output_path, index=False, encoding="utf-8-sig")