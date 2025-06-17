import duckdb
from constants import DATA_WAREHOUSE_PATH

import duckdb
from constants import DATA_WAREHOUSE_PATH

def query_dwh(query: str = "SELECT * FROM mart.mart_technical_jobs"):
    """
    """
    try:
        with duckdb.connect(str(DATA_WAREHOUSE_PATH)) as conn:
            return conn.execute(query).fetchdf()
    except Exception as e:
        raise RuntimeError(f" fel: {e}")
