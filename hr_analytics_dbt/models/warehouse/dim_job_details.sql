-- models/warehouse/dim_job_details.sql

SELECT DISTINCT 
  {{ dbt_utils.generate_surrogate_key([
    'headline',
    'description_text_formatted',
    'employment_type'
  ]) }} AS job_details_id,

  headline,
  description_text_formatted AS description_html_formatted,
  employment_type

FROM {{ ref('stg_job_ads') }}
WHERE headline IS NOT NULL
