{{ config(materialized='view') }}

SELECT
  occupation_group,
  occupation_label,
  COUNT(*) AS antal_annonser,
  MIN(publication_date) AS första_publicering,
  MAX(application_deadline) AS sista_ansökan
FROM {{ ref('stg_job_ads') }}
WHERE occupation_group = 'Hälso- och sjukvård'
GROUP BY occupation_group, occupation_label
ORDER BY antal_annonser DESC
