# Pipeline Documentation

## Extract
Read the raw CSV file with Pandas.

## Transform
- Inspect columns and data types.
- Remove duplicate rows.
- Impute missing age and treatment-cost values for this educational example.
- Aggregate treatment costs by diagnosis and hospital.

## Load
Write the cleaned dataset and summary tables to CSV files.

## Spark Stage
Read the cleaned CSV into a Spark DataFrame and calculate grouped summaries.

## Production Considerations
A real healthcare system should include access controls, encryption, audit logging, de-identification, secure secrets management, data retention policies, and applicable compliance requirements.
