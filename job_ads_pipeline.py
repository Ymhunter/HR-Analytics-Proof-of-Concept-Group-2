import dlt
import requests

# Hämta jobbanonser från olika yrkesområden


@dlt.source
def jobtech_source():
    OCCUPATION_FIELDS = {
        "RPtN_bxG_ExZ": "Försäljning, inköp, marknadsföring",
        "NYW6_mP6_vwf": "Hälso- och sjukvård",
        "ScKy_FHB_7wT": "Hotell, restaurang, storhushåll"
    }

    # Skapa en resurs för varje occupation field
    def make_resource(occupation_id, occupation_name):
        @dlt.resource(name=f"job_ads_{occupation_id}", write_disposition="replace")
        def job_ads():
            url = f"https://jobsearch.api.jobtechdev.se/search?occupation-field={occupation_id}"
            headers = {"Accept": "application/json"}
            response = requests.get(url, headers=headers)
            response.raise_for_status()
            data = response.json().get("hits", [])

            for item in data:
                item["occupation_id"] = occupation_id
                item["occupation_name"] = occupation_name
                yield item

        return job_ads

    # Returnera en lista med alla resurser
    return [make_resource(occ_id, occ_name) for occ_id, occ_name in OCCUPATION_FIELDS.items()]


# Skapa pipeline
pipeline = dlt.pipeline(
    pipeline_name="job_ads_pipeline",
    destination="duckdb",
    dataset_name="raw_job_ads"
)

# Kör pipelinen
load_info = pipeline.run(jobtech_source())
print(load_info)
