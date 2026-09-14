from generator_config import SEED, NUM_SALES, NUM_STORES, NUM_CUSTOMERS, NUM_PRODUCTS, PROMOTION_PROBABILITY
import numpy as np
import pandas as pd
from pathlib import Path

rng=np.random.default_rng(SEED)

payment_types=[
    "Készpénz",
    "Bankkártya",
    "Utalvány"
]
sales=[]

data_path = Path(__file__).parent.parent / "data"
products = pd.read_csv(data_path / "products.csv")
promotions=pd.read_csv(data_path / "promotions.csv")
promotions["start_date"] = pd.to_datetime(promotions["start_date"])
promotions["end_date"] = pd.to_datetime(promotions["end_date"])

for i in range(1, NUM_SALES + 1):
    product_id = rng.integers(1, NUM_PRODUCTS + 1)
    unit_price = products.loc[products["product_id"] == product_id,"unit_price"].iloc[0]
    quantity = rng.integers(1, 10)
    total_price = unit_price * quantity
    sales_date = pd.Timestamp("2026-01-01") + pd.Timedelta(days=int(rng.integers(0, 365)))



    promotion_id=None

    product_promotion=promotions.loc[promotions["product_id"]==product_id]

    if  not product_promotion.empty:
        valid_promotions=product_promotion.loc[(product_promotion["start_date"]<=sales_date)
                                                & (product_promotion["end_date"]>=sales_date)]
        if not valid_promotions.empty and rng.random() < PROMOTION_PROBABILITY:
            promotion_id = rng.choice(valid_promotions["promotion_id"].to_numpy()
)
    sales.append({
        "sales_id": i,
        "sales_date":sales_date,
        "store_id":rng.integers(1, NUM_STORES + 1),
        "customer_id":rng.integers(1, NUM_CUSTOMERS + 1),
        "product_id":product_id,
        "promotion_id":promotion_id,
        "quantity": quantity,
        "unit_price": unit_price,
        "total_price": total_price,
        "payment_type": rng.choice(payment_types)


    })

output_path = Path(__file__).parent.parent / "data" / "sales.csv"
sales_df = pd.DataFrame(sales)
sales_df.to_csv(output_path, index=False, encoding="utf-8-sig")