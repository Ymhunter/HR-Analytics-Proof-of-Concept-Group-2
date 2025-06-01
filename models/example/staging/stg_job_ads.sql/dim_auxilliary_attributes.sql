{{ config(materialized='table') }}

SELECT
    duration_label,
    publication_date,
    application_deadline,
    working_hours AS working_hours_label
FROM {{ ref('stg_job_ads') }}
WHERE duration_label IS NOT NULL