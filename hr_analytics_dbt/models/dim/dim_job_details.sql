WITH job_ads AS (
    SELECT *
    FROM {{ ref('src_job_details') }}
)

SELECT 
    {{ dbt_utils.generate_surrogate_key(["id"]) }} AS job_details_id,
    headline,
    description__text AS description,
    description__text_formatted,
    employment_type__label AS employment_type,
    duration__label AS duration,
    salary_type__label AS salary_type,
    scope_of_work__min,
    scope_of_work__max
FROM job_ads
