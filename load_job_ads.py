import dlt
import duckdb
import requests
from datetime import datetime

# DLT pipeline initiering
pipeline = dlt.pipeline(
    pipeline_name="job_ads_pipeline",
    destination="duckdb",
    dataset_name="job_ads_data"
)

# Yrkesområden ni valt (occupation fields)
occupation_fields = [
    "Försäljning, inköp, marknadsföring",
    "Hälso- och sjukvård",
    "Hotell, restaurang, storhushåll"
]
