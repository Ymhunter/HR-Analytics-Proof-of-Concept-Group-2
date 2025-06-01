{{ config(materialized='table') }}

SELECT *
FROM {{ ref('fct_job_ads') }}
WHERE occupation_group__label = 'Hälso- och sjukvård'
