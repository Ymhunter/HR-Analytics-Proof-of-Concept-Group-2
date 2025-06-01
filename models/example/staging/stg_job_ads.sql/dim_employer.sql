{{ config(materialized='table') }}

SELECT DISTINCT
    employer_id,
    employer_name,
    employer_workplace,
    employer_organization_number,
    region AS workplace_region,
    municipality AS workplace_city,
    workplace_address AS workplace_street_address,
    workplace_postcode,
    workplace_country
FROM {{ ref('stg_job_ads') }}