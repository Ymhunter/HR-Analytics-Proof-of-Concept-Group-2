Kör dlt_ingest.py med Python 3.11. 

1. Skapa virtuell miljö:
   uv venv .venv
   .venv\Scripts\Activate.ps1

2. Installera paket:
   uv pip install -r requirements.txt

3. Kör skriptet:
   python dlt_ingest.py

Data hämtas från JobTech API och sparas i job_ads.duckdb via DLT och DuckDB.