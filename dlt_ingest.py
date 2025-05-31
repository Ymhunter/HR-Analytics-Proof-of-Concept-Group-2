import requests # För att skicka anrop till jobtech 
import duckdb # För att spara datan i Duckdb
import pandas as pd # För att hantera json som en tabell
import dlt  # dlt biblioteket som hanterar dataloading

# Skapat pipeline med namn och målformat (Ducckdb)
pipeline = dlt.pipeline(
    pipeline_name="job_ads_pipeline",
    destination="duckdb",
    dataset_name="job_ads"
)
# Yrkesområden och id
occupations = [
    "RPTn_bxG_ExZ",  # Försäljning, inköp, marknadsföring
    "NYW6_mP6_wvf",  # Hälso och sjukvård
    "ScKy_FHB_7wT"   # Hotell, restaurang, storhushåll
]
