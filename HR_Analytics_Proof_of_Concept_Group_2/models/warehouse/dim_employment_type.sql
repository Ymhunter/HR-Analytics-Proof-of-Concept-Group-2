select distinct
    employment_type
from {{ ref('stg_job_ads') }}
where employment_type is not null
