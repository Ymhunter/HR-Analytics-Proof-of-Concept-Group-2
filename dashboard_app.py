# Importerar nödvändiga bibliotek
import streamlit as st
import duckdb
import pandas as pd

# Skapar en anslutning till Duckdb databasen
con = duckdb.connect("job_ads.duckdb")

# Sätter en titel och underrubrik för dashboarden
st.title("Hr analysinstrument")
st.subheader("Analys av jobbannonser per yrkesområde")

# Dropdown meny för att välja mart-vy (yrkesområde)
mart_val = st.selectbox("Välj yrkesområde:", [
    "sales_mart",
    "health_mart",
    "hospitality_mart"
])

# Ladda data från vald mart-vy
df = con.execute(f"SELECT * FROM {mart_val}").fetchdf()
#Visar tabell 
st.dataframe(df)
st.write("Kolumner i datan:", df.columns.tolist())
st.write("Antal rader i datan:", len(df))

# Kolla vilken kolumn som finns för yrkesroll
occupation_col = "occupation_label" if "occupation_label" in df.columns else "occupation"

#Visualisering 1: Antal annonser per yrkesroll
st.subheader("Antal annonser per yrkesroll")
occupation_counts = df[occupation_col].value_counts().reset_index()
occupation_counts.columns = ["Yrkesroll", "Antal annonser"]
st.bar_chart(occupation_counts.set_index("Yrkesroll"))

#Visualisering 2: Visar de fem yrkesroller med flest annonser
st.subheader("Topp 5 yrkesroller med flest annonser")
top_5 = occupation_counts.sort_values("Antal annonser", ascending=False).head(5)
st.bar_chart(top_5.set_index("Yrkesroll"))

#Visualisering 3:Grupperar efter duration_label
st.subheader("Antal annonser per annonseringsperiod")
duration_counts = df["duration_label"].value_counts().reset_index()
duration_counts.columns = ["Annonsperiod", "Antal annonser"]
st.bar_chart(duration_counts.set_index("Annonsperiod"))

# Visualisering 4:  Räknar antal annonser per datum då de först publicerades
st.subheader("Antal annonser över tid")
df['publication_date'] = pd.to_datetime(df['publication_date'])
time_counts = df['publication_date'].dt.to_period('M').value_counts().sort_index()
time_counts.index = time_counts.index.to_timestamp()
st.line_chart(time_counts)

# Visualisering 5: Antal annonser per stad
st.subheader("Antal annonser per stad")
if "workplace_city" in df.columns:
    city_counts = df["workplace_city"].value_counts().reset_index()
    city_counts.columns = ["Stad", "Antal annonser"]
    st.bar_chart(city_counts.set_index("Stad"))
else:
    st.warning("Inget fält för stad hittades i datan.")

