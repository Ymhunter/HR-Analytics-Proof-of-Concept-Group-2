WITH job_ads AS (
    SELECT *
    FROM {{ ref('src_job_details') }}
)

SELECT 
    {{ dbt_utils.generate_surrogate_key(["occupation__concept_id"]) }} AS occupation_id,
    occupation__label AS occupation,
    occupation_group__label AS occupation_group,
    occupation_field__label AS occupation_field
FROM job_ads
