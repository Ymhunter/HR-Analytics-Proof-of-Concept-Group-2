-- models/mart/job_ads_sales.sql

SELECT *
FROM {{ ref('fct_job_ads') }}
WHERE occupation_field = 'FÃ¶rsÃ¤ljning, inkÃ¶p, marknadsfÃ¶ring'
