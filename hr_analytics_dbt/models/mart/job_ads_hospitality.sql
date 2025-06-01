-- models/mart/job_ads_hospitality.sql

SELECT *
FROM {{ ref('fct_job_ads') }}
WHERE occupation_field = 'Hotell, restaurang, storhushÃ¥ll'
