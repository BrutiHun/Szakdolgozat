from pathlib import Path
import runpy

base_path = Path(__file__).parent
data_path= base_path / "data"

data_path.mkdir(exist_ok=True)

generators=[
    "regions_generator",
    "products_generator",
    "promotions_generator",
    "stores_generator",
    "customers_generator",
    "sales_generator"
]
for generator in generators:
    print(f"Running {generator}")
    runpy.run_path(base_path/"data_generator"/f"{generator}.py")

generators=[
    "products_error",
    "promotions_error",
    "stores_error",
    "customers_error",
    "sales_error"
]
for generator in generators:
    print(f"Running {generator}")
    runpy.run_path(base_path/"error_generator"/f"{generator}.py")