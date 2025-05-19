select distinct
    city
from {{ ref('stg_job_ads') }}
where city is not null
