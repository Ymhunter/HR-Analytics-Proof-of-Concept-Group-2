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

API_URL = "https://jobsearch.api.jobtechdev.se/search"


def fetch_jobs_for_field(field):
    params = {
        "occupation-field": field,
        "limit": 100
    }
    response = requests.get(API_URL, params=params)
    response.raise_for_status()
    return response.json()["hits"]
