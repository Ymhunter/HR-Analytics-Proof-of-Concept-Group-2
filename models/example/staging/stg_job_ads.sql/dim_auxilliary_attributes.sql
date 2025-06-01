{{ config(materialized='table') }}

SELECT DISTINCT
    auxilliary_attributes_id,
    has_driving_license AS driver_license,
    needs_car AS access_to_own_car,
    experience_required
FROM {{ ref('stg_job_ads') }}