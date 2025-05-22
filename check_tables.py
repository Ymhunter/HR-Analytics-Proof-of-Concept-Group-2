import duckdb

# Anslut till din databasfil
con = duckdb.connect('job_ads_pipeline.duckdb')

# Lista alla tabeller
print("Tabeller i databasen:")
print(con.execute("SHOW TABLES").fetchall())

# Räkna rader i varje tabell
print("\nAntal rader i varje tabell:")
tables = con.execute("SHOW TABLES").fetchall()
for table in tables:
    table_name = table[0]
    count = con.execute(f"SELECT COUNT(*) FROM {table_name}").fetchone()[0]
    print(f"{table_name}: {count} rader")
