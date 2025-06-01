{{ config(materialized='table') }}

SELECT
    occupation_id,
    job_details_id,
    employer_id,
    auxilliary_attributes_id,
    number_of_vacancies AS vacancies,
    relevance,
    application_deadline
FROM {{ ref('stg_job_ads') }}
WHERE occupation_id IS NOT NULL