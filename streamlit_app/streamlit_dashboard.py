import streamlit as st
import duckdb
import pandas as pd

# Titel i dashboarden
st.title("Job Ads Dashboard")

# 🟢 Anslut till DuckDB-filen
con = duckdb.connect("../job_ads_pipeline.duckdb")

# 🔵 Ladda in unika occupation_fields
occupation_fields = con.execute("""
    SELECT DISTINCT occupation_field FROM fct_job_ads
""").fetchdf()

selected_field = st.selectbox(
    "Välj yrkesområde", occupation_fields["occupation_field"]
)

# 🟡 Filtrera efter valt yrkesområde
query = f"""
    SELECT * FROM fct_job_ads
    WHERE occupation_field = '{selected_field}'
"""

df = con.execute(query).fetchdf()

# 🔴 Visa antal annonser som KPI
st.metric(label="Antal annonser", value=len(df))

# 🟣 Visa hela tabellen
st.dataframe(df)
