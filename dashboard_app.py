# Importerar nödvändiga bibliotek
import streamlit as st
import duckdb
import pandas as pd

# Skapar en anslutning till DuckDB-databasen
con = duckdb.connect("job_ads_pipeline.duckdb")

# Sätter en titel och underrubrik för dashboarden
st.title("Hr analysintsrument")
st.subheader("Analys av jobbannonser per yrkesområde")

