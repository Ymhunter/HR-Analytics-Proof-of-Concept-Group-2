# Importerar bibliotek för datahantering, API-anrop och databaslagring
import dlt # Används för att skapa och köra pipelines
import requests # Används för att hämta data via HTTP från JobTech API
import duckdb # Används för att lagra och läsa data lokalt i DuckDB

# Skapar en DLT-pipeline som kommer att hantera datainladdning till en lokal DuckDB-databas
pipeline = dlt.pipeline( 
    pipeline_name="job_ads_pipeline",
    destination="duckdb",
    dataset_name="job_ads"
)
# Definierar en lista med yrkesområden som projektgruppen fokuserar på.
# Dessa används som sökparametrar för att hämta relevanta jobbannonser från JobTech API.
occupations = [
    "Försäljning, inköp, marknadsföring",
    "Hälso och sjukvård",
    "Hotell, restaurang, storhushåll"
]
# Funktion som hämtar annonser från Jobtech apin baserat på våra yrkesområden
def fetch_job_ads():
    base_url = "https://jobsearch.api.jobtechdev.se/search"
    headers = {"accept": "application/json"}
    
    for occupation in occupations:
        params = {
            "q": occupation,
            "limit": 20,  # antal annonser per yrkesområde
        }
        response = requests.get(base_url, headers=headers, params=params) # Skickar förfrågan till apin med rätt parametrar
        data = response.json() # Tolkar svaret från apin som json och sparar det som en python dict
        job_ads = data.get("hits", [])  # Hämtar ut själva annonserna hits från svaret eller en tom lista om nyckeln saknas
        
        for ad in job_ads: 
            ad["occupation_group"] = occupation  # Taggar annonsen med yrkesområde för enklare analys
            yield ad # Returnerar en annons i taget 

# Kör pipelinen med funktionen som hämtar jobbannonser
load_info = pipeline.run(fetch_job_ads())

# Bekräftelse på att datan laddats in till Duckdb
print("Data har laddats till Duckdb!")
print(load_info)
