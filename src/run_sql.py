from pathlib import Path
import sqlite3
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
DATA_DIR = ROOT / "data"
CLEAN_FILE = DATA_DIR / "clean_healthcare_data.csv"
SQL_FILE = ROOT / "sql" / "healthcare_queries.sql"
DATABASE_FILE = DATA_DIR / "healthcare.db"


def run_sql():
    if not CLEAN_FILE.exists():
        raise FileNotFoundError(
            "Cleaned data is missing. Run src/pipeline.py first."
        )

    clean_df = pd.read_csv(CLEAN_FILE)
    sql_text = SQL_FILE.read_text(encoding="utf-8")

    # Remove full-line comments from this project's SQL file.
    sql_lines = [
        line
        for line in sql_text.splitlines()
        if not line.strip().startswith("--")
    ]

    # These three simple queries are separated by semicolons.
    queries = [
        query.strip()
        for query in "\n".join(sql_lines).split(";")
        if query.strip()
    ]

    report_names = [
        "total_cost_by_diagnosis",
        "average_cost_by_hospital",
        "patient_count_by_diagnosis",
    ]

    if len(queries) != len(report_names):
        raise ValueError(
            "Expected exactly three queries in healthcare_queries.sql."
        )

    with sqlite3.connect(DATABASE_FILE) as connection:
        clean_df.to_sql(
            "healthcare",
            connection,
            if_exists="replace",
            index=False,
        )

        print(f"Loaded {len(clean_df)} records into SQLite.")

        for name, query in zip(report_names, queries):
            result = pd.read_sql_query(query, connection)

            output_file = DATA_DIR / f"sql_{name}.csv"
            result.to_csv(output_file, index=False)

            print(f"\n{name.replace('_', ' ').upper()}")
            print(result.to_string(index=False))
            print(f"Saved: {output_file}")

    print(f"\nDatabase saved: {DATABASE_FILE}")
    print("SQL analysis completed.")


if __name__ == "__main__":
    run_sql()