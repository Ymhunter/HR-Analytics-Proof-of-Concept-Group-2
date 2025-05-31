# 📊 HR Analytics – Automatiserad analys av jobbannonser

## 📌 Projektbeskrivning

Detta projekt är ett proof of concept för att hjälpa rekryterare på ett HR-företag att analysera arbetsmarknaden automatiskt. Med hjälp av moderna verktyg har vi byggt en komplett datapipeline som hämtar, strukturerar och visualiserar jobbannonser från Arbetsförmedlingen via Jobtech API.

---

## 🎯 Syfte

- Automatisera hämtning och rensning av jobbannonser
- Identifiera trender inom specifika yrkesområden
- Minska manuell hantering och förbättra beslutsstöd
- Arbeta som ett effektivt datateam med GitHub

---

## 🔧 Teknikstack

| Verktyg         | Funktion                                |
|------------------|-----------------------------------------|
| **DLT**          | Extraktion och laddning av data från API |
| **DuckDB**       | Lagring av rå- och transformerad data    |
| **dbt**          | Datatransformation enligt dimensional modell |
| **Streamlit**    | Visualisering av KPI:er och trender      |
| **Git + GitHub** | Samarbete och versionshantering         |
| **GitHub Projects** | Agil utveckling med Kanban-board       |

---

## 🔄 Datapipeline – Detaljerat flöde

### 1. 🛠️ **Extraktion – DLT + Jobtech API**
- 📄 **Kod:** `dlt_pipeline/load_jobtech.py`
- 🔗 **API:** [https://jobsearch.api.jobtechdev.se/search](https://jobsearch.api.jobtechdev.se/search)
- 📥 **Filter:** yrkesområde (`Försäljning, inköp, marknadsföring,Hälso- och sjukvårdHotell, restaurang, storhushåll`)
- 🗃️ **Output:** Lagrar rådata i DuckDB, `raw` schema

### 2. 🗂️ **Lagring – DuckDB**
- Lagrar alla steg från rådata till färdiga vyer
- 📁 **Schemas:**
  - `raw`: inkommande data från DLT
  - `staging`: rensad och standardiserad data
  - `warehouse`: faktatabell + dimensioner
  - `mart`: aggregerade vyer för dashboard

### 3. 🔄 **Transformation – dbt**
- 📁 **Struktur:**
  - `models/staging/` – t.ex. `stg_job_ads.sql`
  - `models/warehouse/` – t.ex. `dim_employer.sql`, `dim_job_details.sql`
  - `models/marts/` – t.ex. `job_ads_health.sql`
- 🧱 **Datamodell:** Star schema med:
  - `fact_job_ads`
  - `dim_occupation`
  - `dim_city`
  - `dim_employment_type`

### 4. 📊 **Visualisering – Streamlit Dashboard**
- 📄 **Kod:** `streamlit/app.py`
- 📌 **Funktioner:**
  - Visa antal annonser per yrke, stad, anställningstyp
  - Visa trender över tid
  - Filtrera på yrkesområde
  - Presentera nyckeltal (KPI)

