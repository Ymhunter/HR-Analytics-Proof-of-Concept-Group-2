import streamlit as st
import pandas as pd
import duckdb

st.title("Job Ads Dashboard")

# Anslut till databasen
con = duckdb.connect(database="./job_ads_pipeline.duckdb", read_only=True)

# Hämta alla yrkesområden
occupation_fields = con.execute("""
    SELECT DISTINCT occupation_field FROM fct_job_ads
""").fetchdf()

# Dropdown för att välja område
selected_field = st.selectbox(
    "Välj yrkesområde", occupation_fields["occupation_field"])

# Visa grundläggande statistik
st.subheader("Antal annonser")
df_ads = con.execute(f"""
    SELECT * FROM fct_job_ads WHERE occupation_field = '{selected_field}'
""").fetchdf()
st.metric(label="Totalt antal annonser", value=len(df_ads))

# Visa annonserna i tabell
st.dataframe(df_ads)

# Topp 5 yrken (baserat på jobb-titel/headline)
st.subheader("Topp 5 annonserade roller (baserat på titel)")

df_top_roles = con.execute(f"""
    SELECT d.headline, COUNT(*) AS antal
    FROM fct_job_ads f
    JOIN dim_job_details d ON f.job_details_id = d.job_details_id
    WHERE f.occupation_field = '{selected_field}' AND d.headline IS NOT NULL
    GROUP BY d.headline
    ORDER BY antal DESC
    LIMIT 5
""").fetchdf()

st.bar_chart(df_top_roles.set_index("headline"))


st.bar_chart(df_top_roles.set_index("headline"))

# Topp 5 städer
st.subheader("Topp 5 städer")

df_top_cities = con.execute(f"""
    SELECT e.workplace_city, COUNT(*) AS antal
    FROM fct_job_ads f
    JOIN dim_employer e ON f.employer_id = e.employer_id
    WHERE f.occupation_field = '{selected_field}' AND e.workplace_city IS NOT NULL
    GROUP BY e.workplace_city
    ORDER BY antal DESC
    LIMIT 5
""").fetchdf()

st.bar_chart(df_top_cities.set_index("workplace_city"))


# Anställningsformer
st.subheader("Anställningsformer")

df_contracts = con.execute(f"""
    SELECT d.employment_type, COUNT(*) AS antal
    FROM fct_job_ads f
    JOIN dim_job_details d ON f.job_details_id = d.job_details_id
    WHERE f.occupation_field = '{selected_field}' AND d.employment_type IS NOT NULL
    GROUP BY d.employment_type
    ORDER BY antal DESC
""").fetchdf()

st.bar_chart(df_contracts.set_index("employment_type"))

# Topp 5 arbetsgivare
st.subheader("Topp 5 arbetsgivare (baserat på antal annonser)")

df_top_employers = con.execute(f"""
    SELECT e.employer_name, COUNT(*) AS antal
    FROM fct_job_ads f
    JOIN dim_employer e ON f.employer_id = e.employer_id
    WHERE f.occupation_field = '{selected_field}'
    GROUP BY e.employer_name
    ORDER BY antal DESC
    LIMIT 5
""").fetchdf()

st.bar_chart(df_top_employers.set_index("employer_name"))
