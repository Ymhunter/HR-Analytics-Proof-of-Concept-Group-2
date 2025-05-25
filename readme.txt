Kör dlt_ingest.py med Python 3.11. 

1. Skapa virtuell miljö:
   uv venv .venv
   .venv\Scripts\Activate.ps1

2. Installera paket:
   uv pip install -r requirements.txt

3. Kör skriptet:
   python dlt_ingest.py

Uppgift 2:
Data hämtas från Jobtech apin sparas i job_ads.duckdb via dlt och Duckdb.

I denna del av projektet har jag använt biblioteket dlt för att hämta jobbannonser från Jobtechs öppna apin, filtrerat på tre fördefinierade yrkesområden:

Försäljning, inköp, marknadsföring  
Hälso- och sjukvård  
Hotell, restaurang, storhushåll  

Datan laddas ner via ett Python-skript (`dlt_ingest.py`) och lagras lokalt i en Duckdb-databas (`job_ads.duckdb`). Varje annons taggas med sitt yrkesområde för att kunna användas i vidare analys.

Så här körs ingestion skriptet:
```bash
python dlt_ingest.py

Uppgift 4: 
