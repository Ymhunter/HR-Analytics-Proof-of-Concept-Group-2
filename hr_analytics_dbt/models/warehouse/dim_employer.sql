SELECT
    DISTINCT employer_id,
    employer_name,
    webpage_url,
    employer_organization_number,
    workplace_street_address,
    workplace_region,
    workplace_postcode,
    workplace_city,
    workplace_country
FROM {{ ref('stg_job_ads') }}
WHERE employer_id IS NOT NULL
