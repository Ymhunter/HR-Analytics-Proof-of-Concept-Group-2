select *
from {{ ref('fact_job_ads') }}
where occupation ilike any (array[
    '%data%',
    '%software%',
    '%developer%',
    '%it%',
    '%system%'
])
