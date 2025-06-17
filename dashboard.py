# dashboard.py

import streamlit as st
import plotly.express as px
from connect_data_warehouse import query_dwh

st.set_page_config(layout="wide")

def main():
    st.title("💼 HR Talent Insights Dashboard")
    st.markdown("Visual insights to support recruitment for specific occupations.")

    #FILTERS
    fields_df = query_dwh("SELECT DISTINCT occupation_field FROM mart.mart_technical_jobs WHERE occupation_field IS NOT NULL")
    fields = fields_df["occupation_field"].tolist()
    selected_field = st.selectbox("Select Occupation Field", fields)

    df = query_dwh(f"""
        SELECT *
        FROM mart.mart_technical_jobs
        WHERE occupation_field = '{selected_field}'
    """)

    #KPIs
    col1, col2, col3, col4 = st.columns(4)
    col1.metric("📊 Total Vacancies", int(df["vacancies"].sum()))
    col2.metric("🧠 Unique Occupations", df["occupation"].nunique())
    col3.metric("🏢 Employers Hiring", df["employer_name"].nunique())
    top_occ = df.groupby("occupation")["vacancies"].sum().idxmax()
    col4.metric("🔥 Top Role", top_occ)

    st.divider()
    top_occ_df = df.groupby("occupation")["vacancies"].sum().sort_values(ascending=False).reset_index()
    fig1 = px.bar(top_occ_df.head(10), x="vacancies", y="occupation", orientation="h",
                  title="Top Occupations by Number of Vacancies")
    st.plotly_chart(fig1, use_container_width=True)

    #Cities 
    top_cities = df.groupby("workplace_address__city")["vacancies"].sum().sort_values(ascending=False).reset_index()
    fig2 = px.bar(top_cities.head(10), x="vacancies", y="workplace_address__city", orientation="h",
                  title="Top Cities Hiring")
    st.plotly_chart(fig2, use_container_width=True)

    # Employers
    top_employers = df.groupby("employer_name")["vacancies"].sum().sort_values(ascending=False).reset_index()
    fig3 = px.bar(top_employers.head(10), x="vacancies", y="employer_name", orientation="h",
                  title="Top Hiring Employers")
    st.plotly_chart(fig3, use_container_width=True)

    #Duration distribution
    duration_df = df.groupby("duration")["vacancies"].sum().reset_index()
    fig4 = px.pie(duration_df, names="duration", values="vacancies",
                  title="Vacancy Distribution by Job Duration")
    st.plotly_chart(fig4, use_container_width=True)

    #Salary types
    salary_df = df.groupby("salary_type")["vacancies"].sum().reset_index()
    fig5 = px.bar(salary_df, x="salary_type", y="vacancies",
                  title="Vacancies by Salary Type")
    st.plotly_chart(fig5, use_container_width=True)

if __name__ == "__main__":
    main()
