{{ config(materialized='table') }}

SELECT
    employer_name,
    employer_url,
    employer__organization_number
FROM {{ ref('stg_job_ads') }}
WHERE employer_name IS NOT NULL
