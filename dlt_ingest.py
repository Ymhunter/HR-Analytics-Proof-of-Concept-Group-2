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
