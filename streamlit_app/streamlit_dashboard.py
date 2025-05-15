import streamlit as st
import duckdb
import pandas as pd

# Titel i dashboarden
st.title("Job Ads Dashboard")

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
