import duckdb

con = duckdb.connect('job_ads.duckdb')

# Lista med tabeller vi vill kolla
tables = [
    'fct_job_ads',
    'health_mart',
    'hospitality_mart',
    'sales_mart'
]

# Loopar igenom varje tabell och skriver ut occupation_group__label
for table in tables:
    print(f"\nYrkesgrupper i {table}:\n" + "-"*40)
    try:
        result = con.execute(f"SELECT DISTINCT occupation_group__label FROM {table}").fetchall()
        if result:
            for row in result:
                print("-", row[0])
        else:
            print("Inga värden hittades.")
    except Exception as e:
        print(f"Fel vid hämtning från {table}: {e}")

con.close()
