from pathlib import Path
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
DATA_DIR = ROOT / "data"
RAW_FILE = DATA_DIR / "raw_healthcare_data.csv"
CLEAN_FILE = DATA_DIR / "clean_healthcare_data.csv"


def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    original_rows = len(df)
    duplicate_rows = int(df.duplicated().sum())

    print("\nDATA QUALITY REPORT")
    print(f"Raw records: {original_rows}")
    print(f"Duplicate records: {duplicate_rows}")

    df = df.drop_duplicates().copy()

    missing_age = int(df["age"].isna().sum())
    missing_cost = int(df["treatment_cost"].isna().sum())

    print(f"Missing ages after removing duplicates: {missing_age}")
    print(f"Missing costs after removing duplicates: {missing_cost}")

    df["age"] = df["age"].fillna(df["age"].median())
    df["treatment_cost"] = df["treatment_cost"].fillna(
        df["treatment_cost"].median()
    )

    print(f"Clean records: {len(df)}")
    print(f"Remaining missing ages: {df['age'].isna().sum()}")
    print(
        f"Remaining missing costs: "
        f"{df['treatment_cost'].isna().sum()}"
    )

    return df


def run_pandas_pipeline():
    raw_df = pd.read_csv(RAW_FILE)
    clean_df = clean_data(raw_df)

    clean_df.to_csv(CLEAN_FILE, index=False)

    diagnosis_summary = (
        clean_df.groupby("diagnosis", as_index=False)
        .agg(
            total_cost=("treatment_cost", "sum"),
            average_cost=("treatment_cost", "mean"),
            patient_count=("patient_id", "count"),
        )
        .sort_values("total_cost", ascending=False)
    )

    diagnosis_summary.to_csv(
        DATA_DIR / "diagnosis_summary.csv",
        index=False,
    )

    hospital_summary = (
        clean_df.groupby("hospital", as_index=False)
        .agg(
            total_cost=("treatment_cost", "sum"),
            average_cost=("treatment_cost", "mean"),
            patient_count=("patient_id", "count"),
        )
        .sort_values("total_cost", ascending=False)
    )

    hospital_summary.to_csv(
        DATA_DIR / "hospital_summary.csv",
        index=False,
    )

    return clean_df, diagnosis_summary, hospital_summary


def run_spark_pipeline():
    try:
        from pyspark.sql import SparkSession
        from pyspark.sql.functions import avg, count, sum as spark_sum
    except ImportError:
        print("\nPySpark is not installed. Spark stage skipped.")
        return

    spark = (
        SparkSession.builder
        .appName("HealthcareDataEngineeringPipeline")
        .getOrCreate()
    )

    try:
        spark_df = spark.read.csv(
            str(CLEAN_FILE),
            header=True,
            inferSchema=True,
        )

        summary = (
            spark_df.groupBy("diagnosis")
            .agg(
                spark_sum("treatment_cost").alias("total_cost"),
                avg("treatment_cost").alias("average_cost"),
                count("patient_id").alias("patient_count"),
            )
            .orderBy("total_cost", ascending=False)
        )

        print("\nSPARK DIAGNOSIS SUMMARY")
        summary.show()
    finally:
        spark.stop()


if __name__ == "__main__":
    clean, diagnosis_summary, hospital_summary = run_pandas_pipeline()

    print("\nPandas pipeline completed.")

    print("\nDIAGNOSIS SUMMARY")
    print(diagnosis_summary.to_string(index=False))

    print("\nHOSPITAL SUMMARY")
    print(hospital_summary.to_string(index=False))

    print("\nSaved files:")
    print(f"- {CLEAN_FILE}")
    print(f"- {DATA_DIR / 'diagnosis_summary.csv'}")
    print(f"- {DATA_DIR / 'hospital_summary.csv'}")

    run_spark_pipeline()