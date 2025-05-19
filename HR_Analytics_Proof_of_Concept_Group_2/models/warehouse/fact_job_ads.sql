select
    job_id,
    job_title,
    occupation,
    occupation_group,
    city,
    municipality,
    region,
    employment_type,
    work_time,
    employer_name,
    publication_date,
    last_publication_date,
    job_description
from {{ ref('stg_job_ads') }}
