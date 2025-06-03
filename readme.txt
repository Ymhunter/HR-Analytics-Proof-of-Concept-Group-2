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
Data transformerades med hjälp av dbt i tre steg:

Staging
Rådata från Duckdb strukturerades om i en stg_job_ads-modell. Den extraherar och renodlar relevanta kolumner från tabellen job_ads_dataset.job_ads i Duckdb.

Data Warehouse nivå:
En vy kallad job_summary.sql skapade där vi grupperar och sammanfattar jobbannonserna per yrke och publiceringsdatum.

Mart nivå:
Slutligen skapade jag tre mart-modeller som filtrerar annonserna efter de tre yrkesområden vi ansvarar för:

sales_mart.sql (Försäljning, inköp, marknadsföring)

health_mart.sql (Hälso- och sjukvård)

hospitality_mart.sql (Hotell, restaurang, storhushåll)

Dessa modeller kommer senare att användas som underlag för visualiseringar i uppgift 5.

För att köra scriptet
dbt run

Uppgift 5: 
började med en mockad job_ads.csv eftersom det var ett snabbt sätt att få struktur och relationer på plats i stg_job_ads.sql och mart-modellerna.
Det gjorde det enklare att testa dbt pipelinen och dashboarden utan att vara beroende av api anrop 
När flödet fungerade ersattes mocken med korrekt ingestion från jobtech apin i dlt_ingest.py detta visade sig dock att vara ett tidsamt arbete då man fick göra om dlt_ingest.py för apin detta gör jag inte om.
Det positiva var att jag fick en djupare förståelse för hur API-anrop, och datainhämtning fungerar i praktiken. När den riktiga datan väl var på plats kunde jag validera att dashboarden visade relevanta jobbannonser för våra tre yrkesområden. Resultatet blev ett fungerande och automatiserat flöde från jobtech apit till visualisering i Streamlit via duckdb och dbt.