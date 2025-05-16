import streamlit as st
import duckdb
import pandas as pd

# 🟢 Titel i dashboarden
st.title("Job Ads Dashboard")

# 🟢 Anslut till din DuckDB-fil
con = duckdb.connect("../job_ads_pipeline.duckdb")

# 🔵 Ladda in unika occupation_fields
occupation_fields = con.execute("""
    SELECT DISTINCT occupation_field FROM fct_job_ads
""").fetchdf()

selected_field = st.selectbox(
    "Välj yrkesområde", occupation_fields["occupation_field"]
)

# 🟢 Filtrera efter valt yrkesområde
query = f"""
    SELECT * FROM fct_job_ads
    WHERE occupation_field = '{selected_field}'
"""
df = con.execute(query).fetchdf()

# 🔴 Visa antal annonser som KPI
st.metric(label="Antal annonser", value=len(df))

# 🟣 Visa hela tabellen
st.dataframe(df)

# 🟢 Topp 5 yrken inom valt område
st.subheader("Topp 5 yrken inom valt område")
query = f"""
    SELECT d.occupation_name, COUNT(*) AS num_ads
    FROM fct_job_ads f
    JOIN dim_occupation d ON f.occupation_id = d.occupation_id
    WHERE f.occupation_field = '{selected_field}'
    GROUP BY d.occupation_name
    ORDER BY num_ads DESC
    LIMIT 5
"""
df_top5 = con.execute(query).fetchdf()
st.bar_chart(df_top5.set_index("occupation_name"))
