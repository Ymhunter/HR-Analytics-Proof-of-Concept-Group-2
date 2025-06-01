{{ config(materialized='table') }}

SELECT DISTINCT
    job_details_id,
    headline,
    description,
    description_formatted AS description_html_formatted,
    employment_type,
    duration_label AS duration,
    salary_type,
    workhours_from AS scope_of_work_min,
    workhours_to AS scope_of_work_max
FROM {{ ref('stg_job_ads') }}