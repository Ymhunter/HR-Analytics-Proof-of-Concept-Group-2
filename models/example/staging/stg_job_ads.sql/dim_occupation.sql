{{ config(materialized='table') }}

SELECT DISTINCT
    occupation_id,
    occupation_label AS occupation,
    occupation_group,
    occupation_field
FROM {{ ref('stg_job_ads') }}