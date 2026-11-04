from pathlib import Path
import duckdb

DATA_PATH = Path(__file__).parent / "data"

# if run several times, will not crash
DATA_PATH.mkdir(exist_ok=True)

def query_duckdb(sql_code: str, parameters = None):
    with duckdb.connect(DATA_PATH / "movies.duckdb") as conn:
        # add parameters=parameters tom make more secure
        cursor = conn.execute(sql_code, parameters=parameters)

        if sql_code.strip().casefold().startswith(("select", "desc", "from")):
            return cursor.df()

# in video: devided into 2 scirpts, but if you want to keep in one script
# use this guard
if __name__ == "__main__":
    query_duckdb("""sql
        CREATE TABLE IF NOT EXISTS movies(
            title TEXT,
            year INT,
            genre TEXT,
            rating INT,
            summart TEXT
            )
    """)

