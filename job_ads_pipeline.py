import dlt
import requests
from pathlib import Path
import os

# --- API fetcher --- #
def get_ads(params):
    url = "https://jobsearch.api.jobtechdev.se/search"
    response = requests.get(url, params=params)
    response.raise_for_status()
    return response.json()

# --- DLT resource: Loop over occupation fields and yield ads --- #
@dlt.resource(write_disposition="replace")
def jobsearch_multiple_fields():
    occupation_fields = {
        "RPTn_bxG_ExZ": "Försäljning, inköp, marknadsföring",
        "NYW6_mP6_vwf": "Hälso- och sjukvård",
        "ScKy_FHB_7wT": "Hotell, restaurang, storhushåll",

    }

    for field_id, field_name in occupation_fields.items():
        params = {
            "occupation-field": field_id,
            "limit": 100
        }

        data = get_ads(params)
        hits = data.get("hits", [])
        print(f"{field_name}: {len(hits)} ads found")

        for ad in hits:
            # Optionally add field name for easier distinction
            ad["occupation_field_name"] = field_name
            yield ad

# --- Run pipeline --- #
def run_pipeline(table_name, working_directory):
    pipeline = dlt.pipeline(
        pipeline_name='jobsearch_multi',
        destination=dlt.destinations.duckdb(f"{working_directory}/ads_resource.duckdb"),
        dataset_name='staging'
    )

    load_info = pipeline.run(jobsearch_multiple_fields(), table_name=table_name)
    print("Pipeline load info:", load_info)

# --- Main --- #
if __name__ == "__main__":
    working_directory = Path(__file__).parent
    os.chdir(working_directory)

    table_name = "job_ads_all"
    run_pipeline(table_name, working_directory)
