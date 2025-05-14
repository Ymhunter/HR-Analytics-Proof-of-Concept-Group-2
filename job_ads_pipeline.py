import dlt
import requests

# Lista med occupation field ID:n och beskrivningar
OCCUPATION_FIELDS = {
    "RPTn_bxG_ExZ": "Försäljning, inköp, marknadsföring",
    "NYW6_mP6_vwf": "Hälso- och sjukvård",
    "ScKy_FHB_7wT": "Hotell, restaurang, storhushåll"
}


@dlt.source
def jobtech_source():
    for occupation_id, occupation_name in OCCUPATION_FIELDS.items():

        @dlt.resource(name=f"job_ads_{occupation_id}", write_disposition="replace")
        def job_ads():
            url = f"https://jobsearch.api.jobtechdev.se/search?occupation-field={occupation_id}"
            headers = {"Accept": "application/json"}
            response = requests.get(url, headers=headers)
            response.raise_for_status()
            data = response.json().get("hits", [])

            # Lägg till extra fält så vi vet vilket område datan tillhör
            for job in data:
                job["occupation_id"] = occupation_id
                job["occupation_name"] = occupation_name
            return data

        yield job_ads


# Skapa och kör pipeline
pipeline = dlt.pipeline(
    pipeline_name="job_ads_pipeline",
    destination="duckdb",
    dataset_name="raw_job_ads"
)

load_info = pipeline.run(jobtech_source())
print(load_info)
