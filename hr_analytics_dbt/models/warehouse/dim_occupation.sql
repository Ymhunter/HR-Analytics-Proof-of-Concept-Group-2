-- models/warehouse/dim_occupation.sql

SELECT DISTINCT
    occupation_id,
    occupation_name,
    occupation_field
FROM {{ ref('stg_job_ads') }}