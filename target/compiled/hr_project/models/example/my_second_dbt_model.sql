-- Use the `ref` function to select from other models

select *
from "job_ads_pipeline"."main"."my_first_dbt_model"
where id = 1