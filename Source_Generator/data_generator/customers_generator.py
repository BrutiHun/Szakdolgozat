from generator_config import SEED, NUM_CUSTOMERS, NUM_REGIONS
import numpy as np
import pandas as pd
from pathlib import Path
from faker import Faker

rng = np.random.default_rng(SEED)

fake = Faker("hu_HU")
fake.seed_instance(SEED)

customers = []
for i in range(1, NUM_CUSTOMERS + 1):
    gender=rng.choice(["Férfi","Nő"])
    if gender=="Férfi":
        first_name=fake.first_name_male()
    else:
        first_name=fake.first_name_female()
    customers.append({
        "customer_id": i,
        "first_name": first_name,
        "last_name": fake.last_name(),
        "gender":gender,
        "birth_date":fake.date_of_birth(minimum_age=18, maximum_age=80),
        "region_id":rng.integers(1,NUM_REGIONS+1)
        
    })

output_path = Path(__file__).parent.parent / "Data" / "loyalty_customers.csv"
customers_df = pd.DataFrame(customers)
customers_df.to_csv(output_path, index=False, encoding="utf-8-sig")