# Importerar nödvändiga bibliotek
import streamlit as st
import duckdb
import pandas as pd

# Skapar en anslutning till DuckDB-databasen
con = duckdb.connect("job_ads_pipeline.duckdb")

# Sätter en titel och underrubrik för dashboarden
st.title("Hr analysintsrument")
st.subheader("Analys av jobbannonser per yrkesområde")

# Dropdown meny för att välja mart-vy (yrkesområde)
mart_val = st.selectbox("Välj yrkesområde:", [
    "sales_mart", 
    "health_mart", 
    "hospitality_mart"
])

# Laddar data från vald mart vy
df = con.execute(f"SELECT * FROM {mart_val}").fetchdf()

# Visar tabellen
st.dataframe(df)

st.subheader("Antal annonser per yrkesroll")
occupation_counts = df["occupation_label"].value_counts().reset_index()
occupation_counts.columns = ["Yrkesroll", "Antal annonser"]
st.bar_chart(occupation_counts.set_index("Yrkesroll"))

st.subheader("Topp 5 yrkesroller med flest annonser")
top_5 = occupation_counts.sort_values("Antal annonser", ascending=False).head(5)
st.bar_chart(top_5.set_index("Yrkesroll"))

st.subheader("Antal annonser per annonseringsperiod")
duration_counts = df["duration_label"].value_counts().reset_index()
duration_counts.columns = ["Annonseringsperiod", "Antal annonser"]
st.bar_chart(duration_counts.set_index("Annonseringsperiod"))
