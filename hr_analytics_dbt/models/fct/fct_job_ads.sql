

WITH job_ads AS (
    SELECT *
    FROM {{ ref('src_job_details') }}
)

SELECT 
    {{ dbt_utils.generate_surrogate_key(["occupation__concept_id"]) }} AS occupation_id,
    {{ dbt_utils.generate_surrogate_key(["id"]) }} AS job_details_id,
    {{ dbt_utils.generate_surrogate_key(["employer__organization_number"]) }} AS employer_id,
    {{ dbt_utils.generate_surrogate_key(["id", "experience_required", "driving_license_required", "access_to_own_car"]) }} AS auxiliary_attributes_id,
    number_of_vacancies AS vacancies,
    relevance,
    application_deadline
FROM job_ads
