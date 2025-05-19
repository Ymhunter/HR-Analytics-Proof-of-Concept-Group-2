select *
from {{ ref('fact_job_ads') }}
where occupation ilike any (array[
    '%engineer%',
    '%mechanical%',
    '%civil%',
    '%electrical%',
    '%construction%'
])
