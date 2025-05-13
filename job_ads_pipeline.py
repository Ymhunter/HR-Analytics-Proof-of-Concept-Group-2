import dlt
import requests


def fetch_jobs(occupation_fields):
    base_url = "https://jobsearch.api.jobtechdev.se/search"
    limit = 100
    for field in occupation_fields:
        offset = 0
        while True:
            params = {
                'occupation-field': field,
                'limit': limit,
                'offset': offset
            }
            response = requests.get(base_url, params=params)
            response.raise_for_status()
            data = response.json()
            hits = data.get("hits", [])

            if not hits:
                break

            for job in hits:
                yield job

            if len(hits) < limit or offset >= 1900:
                break

            offset += limit

@dlt.source
def jobtech_source():
    occupation_fields = [
        "RPTn_bxG_ExZ", 
        "NYW6_mP6_vwf",  
        "ScKy_FHB_7wT" 
    ]
    return dlt.resource(fetch_jobs(occupation_fields), name="job_ads_pipeline", write_disposition="append")

pipeline = dlt.pipeline(
    pipeline_name="job_ads_pipeline",
    destination="duckdb",
    dataset_name="job_ads_data"
)

info = pipeline.run(jobtech_source())
print(info)
