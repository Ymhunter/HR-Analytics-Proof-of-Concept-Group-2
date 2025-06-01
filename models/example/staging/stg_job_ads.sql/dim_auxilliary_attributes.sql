{{ config(materialized='table') }}

SELECT
    id,
    duration_label,
    publication_date,
    working_hours,
    application_deadline
FROM {{ ref('stg_job_ads') }}
WHERE id IS NOT NULL
