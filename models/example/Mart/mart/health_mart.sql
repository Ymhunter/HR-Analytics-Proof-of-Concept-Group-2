{{ config(materialized='view') }}

SELECT
  occupation_label AS occupation,
  COUNT(*) AS number_of_ads,
  duration_label,
  MIN(publication_date) AS earliest_publication,
  MAX(application_deadline) AS latest_deadline
FROM {{ ref('stg_job_ads') }}
WHERE occupation_group = 'Hälso- och sjukvård'
GROUP BY occupation_label, duration_label
ORDER BY number_of_ads DESC
