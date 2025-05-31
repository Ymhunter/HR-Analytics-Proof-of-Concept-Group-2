import requests # För att skicka anrop till jobtech 
import duckdb # För att spara datan i Duckdb
import pandas as pd # För att hantera json som en tabell
import dlt  # dlt biblioteket som hanterar dataloading

# Skapar pipeline med namn och målformat (Ducckdb)
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

# Funktion som hämtar jobbannonser från apit
def fetch_job_ads():
    base_url = "https://jobsearch.api.jobtechdev.se/search" # api endpoint för jobbsökning
    headers = {"accept": "application/json"} # Header för att ange att vi vill ha svar i JSON-format

    for occupation in occupations: # Loopar igenom varje concept_id (yrkesområde) i listan
        params = {
            "occupation-field": occupation, # Begränsar sökningen till ett yrkesområde
            "limit": 100  # Max 100 annonser per område
        }
        response = requests.get(base_url, headers=headers, params=params)  # Skicka en get förfrågan till apit med parametrarna
        data = response.json()  # Omvandlar json svaret till en Python dict
        job_ads = data.get("hits", [])  # Hämtar ut listan med annonser

        for ad in job_ads: # Loopar igenom 
            ad["occupation_field"] = occupation  # Lägger till yrkesområde i varje annons
            yield ad # Returnerar en annons i taget som en rad i pipelinen

# Kör pipelinen och sparae annonserna till duckdb
load_info = pipeline.run(fetch_job_ads(), table_name="job_ads")

# Skriver ut bekräftelse i terminalen så vi vet att allt gick bra
print("\u2705 Data har laddats in i DuckDB.")
print(load_info) # Visar en sammanfattning av hur många rader som laddades in etc
