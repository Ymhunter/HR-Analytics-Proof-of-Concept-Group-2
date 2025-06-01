{{ config(materialized='table') }}

SELECT
    id,
    occupation_label,
    duration_label,
    publication_date,
    application_deadline,
    working_hours,
    region
FROM {{ ref('stg_job_ads') }}
WHERE occupation_label IS NOT NULL
