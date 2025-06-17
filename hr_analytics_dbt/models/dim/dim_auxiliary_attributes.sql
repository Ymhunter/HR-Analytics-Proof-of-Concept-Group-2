WITH job_ads AS (
    SELECT *
    FROM {{ ref('src_job_details') }}
)

SELECT 
    {{ dbt_utils.generate_surrogate_key(["id", "experience_required", "driving_license_required", "access_to_own_car"]) }} AS auxiliary_attributes_id,
    experience_required,
    driving_license_required AS driver_license,
    access_to_own_car
FROM job_ads
