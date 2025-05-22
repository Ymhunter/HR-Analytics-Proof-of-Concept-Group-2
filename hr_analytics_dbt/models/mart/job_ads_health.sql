-- models/mart/job_ads_health.sql

SELECT *
FROM {{ ref('fct_job_ads') }}
WHERE occupation_field = 'Hälso- och sjukvård'
