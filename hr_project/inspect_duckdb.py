#import duckdb testtabell.

# Anslut till rätt fil
#con = duckdb.connect("job_ads.duckdb")

# Visa alla tabeller och filtrera dem på namespace = 'ads_dataset'
#print("Tillgängliga tabeller i 'ads_dataset':")
#tables = con.execute("SELECT table_name FROM duckdb_tables WHERE database_name = 'job_ads' AND schema_name = 'ads_dataset'").fetchall()
#for t in tables:
#    print("-", t[0])

# Visa kolumner i ads_dataset.job_ads om den finns
#if any(t[0] == "job_ads" for t in tables):
#    print("\nKolumner i ads_dataset.job_ads:")
#    cols = con.execute("PRAGMA table_info('ads_dataset.job_ads')").fetchall()
#    for col in cols:
#        print("-", col[1])
#else:
#    print("\nTabellen 'job_ads' finns inte i datasetet 'ads_dataset'.")
