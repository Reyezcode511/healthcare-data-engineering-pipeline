# Data Dictionary

| Column | Type | Description |
|---|---|---|
| patient_id | integer | Fictional patient identifier |
| age | integer | Example patient age |
| gender | string | Example demographic field |
| diagnosis | string | Example diagnosis category |
| hospital | string | Example hospital category |
| treatment_cost | numeric | Example treatment cost |

## Validation Rules

- IDs should be checked for duplicates.
- Age should be numeric and within a valid domain range.
- Treatment cost should be numeric and non-negative.
- Diagnosis and hospital fields should not be blank.
