import streamlit as st
import duckdb
import pandas as pd

# Titel i dashboarden
st.title("Job Ads Dashboard")

# Ladda in unika occupation_fields
occupation_fields = con.execute(
    "SELECT DISTINCT occupation_field FROM fct_job_ads").fetchdf()
selected_field = st.selectbox(
    "Välj yrkesområde", occupation_fields["occupation_field"])

# Filtrera efter valt yrkesområde
query = f"""
    SELECT * FROM fct_job_ads
    WHERE occupation_field = '{selected_field}'
"""
df = con.execute(query).fetchdf()

# Visa antal annonser som KPI
st.metric(label="Antal annonser", value=len(df))

# Anslut till din DuckDB-fil (ligger i projektroten)
con = duckdb.connect("../job_ads_pipeline.duckdb")

# Exempel: hämta data från mart.vy fct_job_ads
query = """
    SELECT *
    FROM fct_job_ads
    LIMIT 50
"""

df = con.execute(query).fetchdf()

# Visa tabellen
st.dataframe(df)
