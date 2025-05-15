-- models/warehouse/fct_job_ads.sql

SELECT
    job_id,
    occupation_id,
    occupation_name,
    relevance,
    application_deadline,
    employer_name,
    workplace_city
FROM {{ ref('stg_job_ads') }}
