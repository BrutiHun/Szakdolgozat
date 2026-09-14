from generator_config import SEED,NUM_REGIONS
import numpy as np
from pathlib import Path
import pandas as pd
import magyar

rng=np.random.default_rng(SEED)
cities=rng.choice(magyar.telepules, NUM_REGIONS, replace=False)


regions=[]
for i in range (1,NUM_REGIONS+1):
       
    regions.append({
        "region_id": i,
        "country":"Magyarország",
        "city": cities[i-1],
        })


    

output_path = Path(__file__).parent.parent / "Data" / "regions.csv"
regions_df = pd.DataFrame(regions)
regions_df.to_csv(output_path, index=False, encoding="utf-8-sig")