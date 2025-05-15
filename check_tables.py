import duckdb

con = duckdb.connect("job_ads_pipeline.duckdb")

# Lista alla tabeller
tables = con.execute("SHOW TABLES").fetchdf()
print(tables)
