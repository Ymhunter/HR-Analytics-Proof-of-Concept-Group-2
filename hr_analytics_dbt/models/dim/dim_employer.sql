WITH job_ads AS (
    SELECT *
    FROM {{ ref('src_job_details') }}
)

SELECT 
    {{ dbt_utils.generate_surrogate_key(["employer__organization_number"]) }} AS employer_id,
    employer__name AS employer_name,
    employer__workplace,
    employer__organization_number,
    workplace_address__street_address AS workplace_street_address,
    workplace_address__region,
    workplace_address__postcode,
    workplace_address__city,
    workplace_address__country
FROM job_ads
