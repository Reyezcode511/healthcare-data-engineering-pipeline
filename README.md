# Healthcare Data Engineering Pipeline

A learning project by Michael Athan-Obi using Python, Pandas,
SQL, and SQLite to clean fictional healthcare records and
produce analytical summaries.

All records are fictional. No real patient information is used.

## What the pipeline does

- Removes duplicate records.
- Fills missing ages and treatment costs using median values.
- Displays a data quality report.
- Saves cleaned records to CSV.
- Produces diagnosis and hospital summaries.
- Loads cleaned records into SQLite.
- Runs three SQL queries and saves their results.

Median imputation is an educational example, not a rule for
real clinical data.

## Verified results

The sample dataset contains 8 raw records.

After cleaning:
- 1 duplicate record removed.
- 1 missing age filled.
- 1 missing treatment cost filled.
- 7 records remain.
- No missing ages or treatment costs remain.

| Diagnosis | Total treatment cost | Record count |
|---|---:|---:|
| Diabetes | 6100 | 3 |
| Hypertension | 4050 | 3 |
| Asthma | 950 | 1 |

The SQL diagnosis totals match the Pandas results.
Counts represent records with a diagnosis, not necessarily
unique patients.

## Project structure

- `src/pipeline.py` — cleaning and Pandas summaries; optional Spark stage.
- `src/run_sql.py` — SQLite loading and SQL analysis.
- `sql/healthcare_queries.sql` — three analytical queries.
- `data/` — sample data and generated CSV results.
- `docs/` — data dictionary and pipeline documentation.
- `screenshots/` — project images.
- `requirements.txt` — required Python packages.

## Run on Windows

Open a terminal in the project folder.

Create a virtual environment:

```powershell
python -m venv .venv
```

Install dependencies:

```powershell
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
```

Run the cleaning pipeline:

```powershell
.\.venv\Scripts\python.exe src\pipeline.py
```

Run SQL analysis:

```powershell
.\.venv\Scripts\python.exe src\run_sql.py
```

Run the cleaning pipeline before SQL analysis.

## Generated outputs

- `data/clean_healthcare_data.csv`
- `data/diagnosis_summary.csv`
- `data/hospital_summary.csv`
- `data/sql_total_cost_by_diagnosis.csv`
- `data/sql_average_cost_by_hospital.csv`
- `data/sql_patient_count_by_diagnosis.csv`
- `data/healthcare.db`

The virtual environment and generated SQLite database are
excluded from Git. Running the scripts recreates the database.

## Spark status

An optional Spark aggregation stage is included in `pipeline.py`.
It has not been tested in this local setup.

PySpark is not required for the verified Pandas and SQLite stages.
Without PySpark, the script reports that the Spark stage is skipped.

## Future improvements

- Add schema and invalid-value validation.
- Save the data quality report to a file.
- Add automated checks for cleaning and summary totals.
- Test and document the optional Spark stage.
- Expand the fictional sample dataset.
