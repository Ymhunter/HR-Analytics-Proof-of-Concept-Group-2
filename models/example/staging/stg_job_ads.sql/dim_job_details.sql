{{ config(materialized='table') }}

SELECT
    id,
    headline,
    description_text,
    application_deadline,
    publication_date,
    occupation_label
FROM {{ ref('stg_job_ads') }}
WHERE id IS NOT NULL
