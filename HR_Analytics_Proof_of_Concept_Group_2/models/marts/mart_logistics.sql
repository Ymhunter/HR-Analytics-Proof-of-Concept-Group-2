select *
from {{ ref('fact_job_ads') }}
where occupation ilike any (array[
    '%logistics%',
    '%transport%',
    '%supply chain%',
    '%driver%',
    '%freight%'
])
