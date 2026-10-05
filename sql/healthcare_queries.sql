-- Healthcare analytics queries

-- 1. Total cost by diagnosis
SELECT
    diagnosis,
    SUM(treatment_cost) AS total_cost
FROM healthcare
GROUP BY diagnosis
ORDER BY total_cost DESC;

-- 2. Average cost by hospital
SELECT
    hospital,
    AVG(treatment_cost) AS average_cost
FROM healthcare
GROUP BY hospital
ORDER BY average_cost DESC;

-- 3. Patient count by diagnosis
SELECT
    diagnosis,
    COUNT(*) AS patient_count
FROM healthcare
GROUP BY diagnosis
ORDER BY patient_count DESC;
