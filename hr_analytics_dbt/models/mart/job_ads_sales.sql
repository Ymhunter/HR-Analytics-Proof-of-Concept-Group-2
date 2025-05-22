-- models/mart/job_ads_sales.sql

SELECT *
FROM {{ ref('fct_job_ads') }}
WHERE occupation_field = 'Försäljning, inköp, marknadsföring'
