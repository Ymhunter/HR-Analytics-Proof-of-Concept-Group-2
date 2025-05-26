{{ config(materialized='table') }}

SELECT
  occupation_group__label AS occupation_group,
  COUNT(*) AS total_ads,
  MIN(publication_date) AS first_posted,
  MAX(publication_date) AS last_posted
FROM {{ ref('stg_job_ads') }}
GROUP BY occupation_group__label
