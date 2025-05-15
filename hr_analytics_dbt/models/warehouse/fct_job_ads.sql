-- models/warehouse/fct_job_ads.sql

SELECT
  job_id,
  occupation_id,
  {{ dbt_utils.generate_surrogate_key([
    'headline',
    'description_text_formatted',
    'employment_type'
  ]) }} AS job_details_id,
  employer_id,
  NULL AS auxiliary_attributes_id, -- Placeholder
  relevance,
  application_deadline
FROM {{ ref('stg_job_ads') }}
WHERE job_id IS NOT NULL
