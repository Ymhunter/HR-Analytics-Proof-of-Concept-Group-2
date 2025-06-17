with raw_job_ads as (
    select *
   from {{ ref("src_job_details") }}

)

select
  occupation__label,
  id,
  employer_workplace,
  workplace_adress_munciiplatiy,
  relevance,
  application_deadline
from raw_job_ads
