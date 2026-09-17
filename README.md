# Healthcare Data Engineering & Analytics Pipeline

An educational end-to-end data engineering project demonstrating data extraction, cleaning, transformation, aggregation, and analytics using **Python, Pandas, SQL, and Apache Spark**.

> **Privacy note:** All healthcare records are fictional and created for learning. This project does not use real patient information.

## Project Objective

Build a reproducible pipeline that takes raw healthcare records, identifies data-quality issues, cleans the data, and produces analytical summaries.

## Architecture

```text
Raw CSV
   |
   v
Pandas / Python
   |
   +--> Inspect data quality
   +--> Remove duplicate rows
   +--> Handle missing values
   +--> Create cleaned dataset
   |
   v
Clean CSV
   |
   v
Apache Spark
   |
   +--> DataFrame processing
   +--> Grouped aggregations
   +--> Summary outputs
   |
   v
Analytics and documentation
```

## Technology Stack

- Python
- Pandas
- SQL
- Apache Spark / PySpark
- Google Colab or local Python
- Git and GitHub

## Data Quality Problems

The raw dataset intentionally contains:
- A duplicated record
- A missing age value
- A missing treatment-cost value

The cleaning process:
1. Removes duplicate rows.
2. Fills missing age values with the median age.
3. Fills missing treatment cost with the median cost.
4. Writes the cleaned dataset to CSV.

> Median imputation is used only for demonstration. A production healthcare pipeline requires domain-approved rules, validation, governance, security, and privacy controls.

## Repository Structure

```text
healthcare-data-engineering-pipeline/
├── data/
│   ├── raw_healthcare_data.csv
│   ├── clean_healthcare_data.csv
│   ├── diagnosis_summary.csv
│   └── hospital_summary.csv
├── docs/
│   ├── DATA_DICTIONARY.md
│   └── PIPELINE_DOCUMENTATION.md
├── notebooks/
│   └── README.md
├── screenshots/
│   ├── diagnosis_cost.png
│   └── pipeline_overview.png
├── sql/
│   └── healthcare_queries.sql
├── src/
│   └── pipeline.py
├── requirements.txt
├── .gitignore
└── README.md
```

## How to Run

### Google Colab

```bash
pip install pandas pyspark matplotlib
```

Upload the repository files to Colab, then run the Python pipeline.

### Local machine

```bash
git clone <your-repository-url>
cd healthcare-data-engineering-pipeline
pip install -r requirements.txt
python src/pipeline.py
```

## Main Transformations

```python
df = df.drop_duplicates()
df["age"] = df["age"].fillna(df["age"].median())
df["treatment_cost"] = df["treatment_cost"].fillna(
    df["treatment_cost"].median()
)
```

## Spark Aggregation

```python
from pyspark.sql.functions import avg, count, sum

summary = (
    spark_df.groupBy("diagnosis")
    .agg(
        sum("treatment_cost").alias("total_cost"),
        avg("treatment_cost").alias("average_cost"),
        count("patient_id").alias("patient_count")
    )
)
```

## Portfolio Skills Demonstrated

- ETL pipeline design
- Data cleaning and quality checks
- Missing-value handling
- Duplicate detection
- Pandas DataFrames
- SQL aggregation concepts
- Spark DataFrame transformations
- Documentation and repository organization
- Reproducible data processing

## Future Improvements

- Add automated data-quality tests
- Add schema validation
- Use a public, de-identified dataset
- Store data in PostgreSQL
- Add Apache Airflow orchestration
- Add Docker support
- Add GitHub Actions CI/CD
- Add a dashboard layer
- Add data lineage and monitoring

## Disclaimer

This is an educational project and is not intended for clinical decision-making, diagnosis, or production healthcare use.
