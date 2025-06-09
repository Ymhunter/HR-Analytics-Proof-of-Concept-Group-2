{{ config(materialized='view') }}

SELECT
    id,
    headline,
    publication_date,
    application_deadline,
    description__text AS description_text,
    duration__label AS duration_label,
    workplace_address__city AS workplace_city,
    working_hours_type__label AS working_hours,
    occupation__label AS occupation_label,
    occupation_group__label AS occupation_group__label,
    workplace_address__region AS region,
    employer__name AS employer_name,
    employer__organization_number,
    employer__url AS employer_url
FROM ads_dataset.job_ads
WHERE id IS NOT NULL