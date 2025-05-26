{{ config(materialized='view') }}

SELECT
  occupation_label AS occupation,
  COUNT(*) AS number_of_ads,
  duration_label,
  MIN(publication_date) AS first_posted,
  MAX(application_deadline) AS last_day_to_apply
FROM {{ ref('stg_job_ads') }}
WHERE occupation_group = 'Data/IT'
GROUP BY 1, 3
ORDER BY number_of_ads DESC
