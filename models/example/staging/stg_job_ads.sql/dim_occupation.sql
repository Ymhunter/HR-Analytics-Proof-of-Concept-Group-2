{{ config(materialized='table') }}

SELECT
    id,
    occupation_group__label,
    occupation_label,
    publication_date,
    employer__organization_number,
    working_hours
FROM {{ ref('stg_job_ads') }}
WHERE id IS NOT NULL
